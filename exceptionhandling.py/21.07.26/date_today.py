from datetime import datetime,timedelta
def today_date():
    return datetime.now().date()
def yesterday():
    return (datetime.now()-timedelta(days=1)).date()
def tomorrow():
    return (datetime.now()-timedelta(days=-1)).date()
