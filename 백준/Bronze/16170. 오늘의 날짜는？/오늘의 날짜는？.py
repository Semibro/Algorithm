import datetime
now = datetime.datetime.utcnow()
now_time = str(now)
print(f'{now_time[0:4]}')
print(f'{now_time[5:7]}')
print(f'{now_time[8:11]}')