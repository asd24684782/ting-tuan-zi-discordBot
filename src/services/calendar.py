from utills.calendar.calendar import calendar


async def get():
    return await calendar.get_events()


async def post():
    pass
