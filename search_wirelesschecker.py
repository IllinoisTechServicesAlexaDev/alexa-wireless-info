import json



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

