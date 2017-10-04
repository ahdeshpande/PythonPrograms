"""

This program accepts a word (not more than 20 characters) from the user and checks if the last two 
characters contain the character 'T', either in upper or lower case.
It prints if it contains it or not as well prints the number of times it occurs.

Author: Abhiraj Deshpande
Changelog: Initial version 10/03/2017

"""

strInput = input('Enter a word (not more than 20 characters) : ')
iLength = len(strInput)

# check if string length is <= 20
if iLength > 20 :
	print ("Word contains more than 20 characters.")
else:
	# check the last 2 characters

	# len = 0
	if iLength == 0 :
		print ('Blank string')
	# len = 1
	elif iLength == 1 :
			if strInput[0] == 't' or strInput[0] == 'T' :
				print (strInput + " contains letter \'t\' 1 time.")
			else:
				print (strInput + " does not contain letter \'t\'.")
	# len > 1
	else:
		iCount = 0
		if strInput[iLength-1] == 't' or strInput[iLength-1] == 'T' :
			iCount += 1
		if strInput[iLength-2] == 't' or strInput[iLength-2] == 'T' :
			iCount += 1

		if iCount == 0 :
			print (strInput + " does not contain letter \'t\'.")
		else:
			print (strInput + " contains letter \'t\' " + str(iCount) + " times.")
		