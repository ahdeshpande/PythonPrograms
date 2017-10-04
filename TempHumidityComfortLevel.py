"""

This program is used to check the comfort level based on temperature and
humidity levels as follows:

Initial - 70 and 42
Every (Temp-1) Humidity +=4 at least
Every (Temp+1) Humidity -=1.25 at least

Temp less than 66 is uncomfortable
Temp more than 81 is uncomfortable
Temp equal to 70, then humidity must be between 12 and 72

Author: Abhiraj Deshpande
Changelog: Initial version 10/03/2017

"""

initTemp = 70.0
initHumidity = 42.0

minTemp = 66
maxTemp = 81

minHumidity = 12
maxHumidity = 71

strComfortable = "The room is Comfortable"
strHot = "The room is too Hot"
strCold = "The room is too Cold"

inputTemp = float(input('Enter the temperature (degrees) : '))
inputHumidity = float(input('Enter the humidity (%) : '))

tempDiff = abs(inputTemp - initTemp)
humidityDiff = abs(inputHumidity - initHumidity)

if inputTemp < minTemp:
	print (strCold)
elif inputTemp > maxTemp:
	print (strHot)
elif inputTemp < initTemp:
	increase = (tempDiff * 4)
	if increase <= humidityDiff:
		print (strComfortable)
	else:
		print (strCold)
elif inputTemp > initTemp:
	increase = (tempDiff * 1.25)
	if increase <= humidityDiff:
		print (strComfortable)
	else:
		print (strHot)
else:
	if minHumidity < inputHumidity < maxHumidity:
		print (strComfortable)
	elif inputHumidity < minHumidity:
		print (strCold)
	else:
		print (strHot)
		
		
			
		