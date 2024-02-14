from datetime import datetime
x=datetime.now()
x_without_microsec=x.replace(microsecond=0)
print(x_without_microsec)