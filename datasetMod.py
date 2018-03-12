import json
from utils import *



with open('houseA.json', "r") as data_file:
	data = json.load(data_file)

dict_activity = readActivity(data)

dict = gettimepartitioned(data)

dict = updatedict(dict, data)
determineActivity(dict)
#jsonArray = json.dumps(dict, sort_keys=True, indent=4)
#print(jsonArray)