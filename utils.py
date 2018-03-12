import datetime
import json

dateFormat = '%d-%b-%Y %H:%M:%S'

def readActivity(data):
	dict = {}
	for activity in data['activities']:
		dict.update({activity['id']:activity['name']})
	return dict

def gettimepartitioned(data):
	startDate = data['activityData'][0]['start']
	startDateTime = datetime.datetime.strptime(startDate, dateFormat)
	beginTime = startDateTime.replace(second=00)
	endTime = beginTime + datetime.timedelta(seconds=59)

	lastEnd = data['activityData'][len(data['activityData'])-1]['end']
	lastEndTime = datetime.datetime.strptime(lastEnd, dateFormat)
	lastEndTime = lastEndTime.replace(second=59)

	dict = {}

	while (not endTime == lastEndTime):
		dict.update({beginTime.strftime(dateFormat):{}})
		beginTime = beginTime + datetime.timedelta(minutes=1)
		endTime = endTime + datetime.timedelta(minutes=1)
	dict.update({beginTime.strftime(dateFormat):{}})
	return dict

def updatedict(dict, data):
	for activity in data['activityData']:
		start = activity['start']
		end = activity['end']

		start = datetime.datetime.strptime(start, dateFormat) #25-Feb-2008 00:19:32
		end = datetime.datetime.strptime(end, dateFormat)	#25-Feb-2008 00:21:24

		duration = end - start 	#1:52

		beginTime = start.replace(second=00)	#25-Feb-2008 00:19:00
		time = (beginTime + datetime.timedelta(seconds=60)) - start 	#27
		
		if start >= beginTime and end <= (beginTime  + datetime.timedelta(seconds=59)):
			try:
				dict[beginTime.strftime(dateFormat)][str(activity['id'])] = str(end - start)	#{25-Feb-2008 00:19:00 : {6 : 27}}
			except KeyError:
				dict[beginTime.strftime(dateFormat)] = {str(activity['id']) : str(end - start)}	#{25-Feb-2008 00:19:00 : {6 : 27}}
			duration = datetime.timedelta(seconds=00)
		else:
			try:
				dict[beginTime.strftime(dateFormat)][str(activity['id'])] = str(time)	#{25-Feb-2008 00:19:00 : {6 : 27}}
			except KeyError:
				dict[beginTime.strftime(dateFormat)] = {str(activity['id']) : str(time)}	#{25-Feb-2008 00:19:00 : {6 : 27}}
		

		duration -= time 	#1:25
		i = 0
		while duration > datetime.timedelta(seconds=00):
			#print(i)	#0
			
			beginTime += datetime.timedelta(minutes=1)	#25-Feb-2008 00:20:00
			if duration > datetime.timedelta(seconds = 59):
				time = datetime.timedelta(seconds=60)
				duration -= time
			else:
				time = duration
				duration = datetime.timedelta(seconds=00)
			try:
				dict[beginTime.strftime(dateFormat)][str(activity['id'])] = str(time)
			except KeyError:
				dict[beginTime.strftime(dateFormat)] = {str(activity['id']) : str(time)}
			i += 1
	return dict

def second_largest(numbers):
    count = 0
    m1 = m2 = float('-inf')
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1            
            else:
                m2 = x
    return m2 if count >= 2 else None

def determineActivity(dict):
	updated_dict = {}
	for key in dict.keys():
		start = dict[key]
		if bool(start):				
			max_occupation = max()
		else:
			dict[key] = 404
	jsonArray = json.dumps(dict, sort_keys=True, indent=4)
	print(jsonArray)