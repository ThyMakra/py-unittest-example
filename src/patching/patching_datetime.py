import datetime

from .need_patching.add import add_data


def create_data():
    # for example, this function affects the production database,
    # so we shouldn't call this in test
    response = add_data()
    return str(response)


def is_weekday():
    today = datetime.datetime.today()
    return (0 <= today.weekday() < 5)
