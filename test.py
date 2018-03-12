import datetime
dateFormat = '%d-%b-%Y %H:%M:%S'
a = datetime.datetime.strptime("29-Feb-2008 18:41:13", dateFormat)

b = datetime.datetime.strptime("29-Feb-2008 19:21:59", dateFormat)
duration = b - a
while duration > datetime.timedelta(seconds=00):
	print(duration)
	if duration > datetime.timedelta(seconds=60):
		duration -= datetime.timedelta(seconds=60)
	else:
		duration = datetime.timedelta(seconds = 00)
		print(duration)