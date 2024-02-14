from datetime import datetime,timedelta
today=datetime.now().date()

yesterday=today-timedelta(days=1)
tomoroow=today+timedelta(days=1)
print("Yesterday: ",yesterday)
print("Today: ",today)
print("Tomorrow: ",tomoroow)