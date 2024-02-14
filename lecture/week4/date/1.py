from datetime import datetime,timedelta
today=datetime.now().date()
x_date=today-timedelta(days=5)
print(x_date)