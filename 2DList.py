"""

Generates a 2D list such that each element is i + j
i: row
j: column



Author: Abhiraj Deshpande
Changelog: Initial version 10/04/2017

"""

rowCount = 10
colCount = 12

twoDlist = []

print ("2D Structure")
for i in range(0, rowCount):
	rowList = []
	for j in range(0, colCount):
		rowList.append(i+j)
	twoDlist.append(rowList)
	print (rowList)

rowSum = []
# Sum of elements in every row
for i in range(0, len(twoDlist)):
	totalValue = 0
	for j in range(0, len(twoDlist[i])):
		totalValue = totalValue + twoDlist[i][j]
	rowSum.append(totalValue)

print ("\n\nSum of all rows")
print (rowSum)


colSum = []
# Sum of elements in every column
for j in range(0, len(twoDlist[0])):
	totalValue = 0
	# col = []
	for i in range(0, len(twoDlist)):
		totalValue = totalValue + twoDlist[i][j]
	# col.append(totalValue)
	# colSum.append(col)
	colSum.append(totalValue)

print ("\n\nSum of all columns")
print (colSum)