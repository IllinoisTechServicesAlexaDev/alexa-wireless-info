import json
import operator

def search_wirelesschecker(buildingname):
	file = open('data/wirelesschecker.json', 'r')
	wirelesscheckers = json.load(file)['data']

	results = []
	for wirelesschecker in wirelesscheckers:
		#if buildingnumber  != None and buildingnumber  != wirelesschecker['buildingnumber'].lower():  continue
		if buildingname   != None and buildingname.lower() != wirelesschecker['buildingname'].lower():   continue
		results.append(wirelesschecker)
	return results

def search_busy_building():
	file = open('data/wirelesschecker.json', 'r')
	wirelesscheckers = json.load(file)['data']
	results = []
	for wirelesschecker in wirelesscheckers:
		clientdevice = int(wirelesschecker['clientdevices'])
		totalAP = int(wirelesschecker['totalAP'])
		if totalAP == 0:
			break
		else:
			percentage = clientdevice / totalAP
		
		if percentage > 3.5:	
			results.append(wirelesschecker['buildingname'])
	return results

def search_most_connection():
	file = open('data/wirelesschecker.json', 'r')
	wirelesscheckers = json.load(file)['data']
	results = []
	data = {}
	for wirelesschecker in wirelesscheckers:
		buildingname = wirelesschecker['buildingname']
		clientdevice = int(wirelesschecker['clientdevices'])			
		data[buildingname] = clientdevice

	sorted_by_value = sorted(data.items(), key=lambda kv: kv[1], reverse=True)
	building_1 = (sorted_by_value[0][0])
	number_1 = (sorted_by_value[0][1])
	building_2 = (sorted_by_value[1][0])
	number_2 = (sorted_by_value[1][1])
	building_3 = (sorted_by_value[2][0])
	number_3 = (sorted_by_value[2][1])
	
	results = [building_1, number_1, building_2, number_2, building_3, number_3]
	return(results)
