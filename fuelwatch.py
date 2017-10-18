link1 = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=2&Suburb=Mandurah'
link2 = 'http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=4&Suburb=Mindarie&Day=tomorrow'
import urllib.request
import urllib.parse
import io
import time
from lxml import etree
from operator import itemgetter
from urllib.request import urlopen

dictionary = {}
list = []
listTomorrow = []
links = [link1]
tableContent = ""
htmlContent = ""
colour = ""

for link in links:
	response = urlopen(link)
	value = response.read()
	content = etree.iterparse(io.BytesIO(value))
	
	i = 0
	for action, element in content:
		if i == 5:
			list.append(dictionary)
			dictionary = {}
			i = 0
			
		if element.text != None:
			#print(element.tag + "-" + element.text)
				
			if element.tag == "location":
				#location.append(element.text)
				dictionary[element.tag] = element.text
				i = i + 1
				
			elif element.tag == "product":
				dictionary[element.tag] = element.text
				i = i + 1
				
			elif element.tag == "price":
				dictionary[element.tag] = element.text
				i = i + 1
				
			elif element.tag == "address":
				dictionary[element.tag] = element.text
				i = i + 1
				
			elif element.tag == "brand":
				dictionary[element.tag] = element.text
				i = i + 1
				
#the list has a number of dictionary
# list can be sorted but not dictionary (you can sort a list of dictionary)
#sort by price
sortedList = sorted(list, key = itemgetter('price'))

colourContent = '<style style = "text.css">.colour{background-color:#FF0000}</style>'

# for printing the result with backgroun		
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