from datetime import datetime, timedelta
import time

dt = datetime(2018, 1, 1)
dt = datetime.now()
print(dt.strptime("2018/01/01", "%Y/%m/%d"))

dt = datetime.fromtimestamp(time.time())
print(f"{dt.year}/{dt.month}")

dt.strftime("%Y/%m")


print(dt1 > dt2)



duration = dt2 - dt1
