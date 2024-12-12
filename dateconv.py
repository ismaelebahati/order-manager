from datetime import datetime, timedelta


def convert(date_string):
    try:
        date_format = "%d/%m/%Y"
        given_date = datetime.strptime(date_string, date_format)
        start_date = datetime(2000, 1, 1)
        return (given_date - start_date).days
    except ValueError:
        return -1



def convert_back(days):
    start_date = datetime(2000, 1, 1)
    target_date = start_date + timedelta(days=days)
    return target_date.strftime("%d/%m/%Y")
