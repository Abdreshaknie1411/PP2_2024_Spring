from datetime import datetime,timedelta
today=datetime.now().date()
yesterday=today+timedelta(days=1)
x=yesterday-today

print(x.seconds)
