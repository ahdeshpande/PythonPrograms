"""

This program is called Collatz Conjecture
For a positive integer:
odd --> x3 + 1
even --> /2

Follow the above steps untill the number reaches to '1'

Count the number of steps till the number reaches 1; the number itself being
step#1

Author: Abhiraj Deshpande
Changelog: Initial version 10/03/2017

"""
import sys

def odd(num):
	return num*3 + 1

def even(num):
	return num/2

stoppingTime = 1;
# inputNum = int(input("Enter a positive integer: "));
inputNum = int(sys.argv[1])

if inputNum > 1:
	print ("Step \t\t\tNumber")
	print (str(stoppingTime) + "\t\t\t" + str(inputNum))
	while inputNum != 1 :
		if inputNum % 2 == 0:
			inputNum = even(inputNum)
			stoppingTime += 1
			print (str(stoppingTime) + "\t\t\t" + str(inputNum))
		else:
			inputNum = odd(inputNum)
			stoppingTime += 1
			print (str(stoppingTime) + "\t\t\t" + str(inputNum))
	print ("Stopping Time : " + str(stoppingTime))
else:
	print ("Input is non-positive!")