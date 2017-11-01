north = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=2&Region=25'
south = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=2&Region=26'
northTomorrow = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=2&Region=26%Day=tomorrow'
southTomorrow = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=2&Region=25&Day=tomorrow'

import time
from lxml import etree
from operator import itemgetter
from urllib.request import urlopen

dictionary = {}
arrayList = [north, south, northTomorrow, southTomorrow]
array = []
tableContent = ""
htmlContent = ""
colour = ""

for list in arrayList:
	response = urlopen(list)
	value = response.read()
	content = etree.fromstring(value)
	items = content.findall('.//item')
	
	for item in items:
		#dictionary['title'] = item.find('./title').text 
		dictionary['price'] = item.find('./price').text
		#dictionary['description'] = item.find('./description').text
		dictionary['address'] = item.find('./address').text
		dictionary['location'] = item.find('./location').text
		dictionary['brand'] = item.find('./brand').text
		
		array.append(dictionary)
		dictionary = dict()
		
		
	
#the list has a number of dictionary
# list can be sorted but not dictionary (you can sort a list of dictionary)
#sort by price
sortedList = sorted(array, key = itemgetter('price'))

colourContent = '<style style = "text.css">.colour{background-color:#FF0000}</style>'

# for printing the result with background		
#for dict in sortedList:
	#print('{price:5s},{address:35s},{location:30s},{brand:15s}'.format(**dict))
	
	#tableContent += '<tr class = "colour"><td>{price}</td><td>{address}</td><td>{location}</td><td>{brand}</td>'.format(**dict)

now = time.strftime("%c");

for dict in sortedList:
	#print('{price:5s},{address:35s},{location:30s},{brand:15s}'.format(**dict))
	
	tableContent += '<tr><td>{price}</td><td>{address}</td><td>{location}</td><td>{brand}</td>'.format(**dict)
	
htmlContent += colourContent + '<html><head> FuelWatch </head><body> {} <table>{}</table></body></html>'.format(now,tableContent)
	
# to write it into the file 
with open("C:/Users/PRIYANK/workshop/fuelwatch.html", "w") as f:
	f.write(htmlContent)