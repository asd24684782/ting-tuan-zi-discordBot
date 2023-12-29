import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from config.config import get_project_path
import logging

logger = logging.getLogger('calendar')
SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
TOKEN_DIR = get_project_path().joinpath('config/token.json')
CRED_FILE_DIR = get_project_path().joinpath('config/credentials.json')


class Calendar:
    def __init__(self) -> None:
        self.creds = None
        self.verify()

    def verify(self):
        if os.path.exists(TOKEN_DIR):
            self.creds = Credentials.from_authorized_user_file(
                TOKEN_DIR, SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:

                flow = InstalledAppFlow.from_client_secrets_file(
                    CRED_FILE_DIR, SCOPES)
                self.creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(TOKEN_DIR, "w") as token:
                token.write(self.creds.to_json())

    async def get_events(self):
        try:
            service = build("calendar", "v3", credentials=self.creds)

            # Call the Calendar API
            now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
            logger.info("Getting the upcoming 10 events")
            events_result = (
                service.events()
                .list(
                    calendarId="primary",
                    timeMin=now,
                    maxResults=10,
                    singleEvents=True,
                    orderBy="startTime",
                )
                .execute()
            )
            events = events_result.get("items", [])

            if not events:
                logger.info("No upcoming events found.")
                return
            return events

        except HttpError as error:
            logger.warning(f"An error occurred: {error}")


calendar = Calendar()
