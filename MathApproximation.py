"""

Approximate the value of x in polynomial equation
x^3 = 3 - 2sin(x)

Print the value of x and the error

Author: Abhiraj Deshpande
Changelog: Initial version 10/04/2017

"""

import math

xMin = 1.0
xMax = 2.0
xIncrementSteps = 0.0001

minValue = 1.0
xSolution = xMin

x = xMin

while x < xMax:
	value = abs(pow(x,3) - 3 + (2 * math.sin(x)))
	if value < minValue:
		minValue = value
		xSolution = x
	x = x + xIncrementSteps

print ("Value of x = " + str(round(xSolution, 4)))
print ("Error = " + str(minValue))