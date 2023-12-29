
import psycopg2
from psycopg2 import pool
from config.config import get
import logging

logger = logging.getLogger()
config = get()


class Postgres:
    """PostgreSQL Database class."""

    def __init__(self, host, user, password, port, dbName):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__port = port
        self.__dbName = dbName
        try:
            self.__postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(1, 20,
                                                                        user=self.__user,
                                                                        password=self.__password,
                                                                        host=self.__host,
                                                                        port=self.__port,
                                                                        database=self.__dbName)
            if (self.__postgreSQL_pool):
                print("Connection pool created successfully")

        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connecting to PostgreSQL", error)

    async def getConnect(self):
        try:
            conn = self.__postgreSQL_pool.getconn()
            if conn:
                logger.warning('Connection opened successfully.')

        except psycopg2.DatabaseError as e:
            logger.error(e)
            raise e

        finally:
            return conn

    def putConnect(self, conn):
        logger.info('put conn')
        self.__postgreSQL_pool.putconn(conn)


postgres = Postgres(
    host=config.db.host,
    user=config.db.user,
    password=config.db.password,
    port=config.db.port,
    dbName=config.db.name
)
