"""

Compute BMI

Author: Abhiraj Deshpande
Changelog: Initial version 10/04/2017

"""
strMetricSys = ""

fWeight = 0.0

iFeet = 0
iInches = 0

fHeight = 0.0

boolContinue = True

fBMI = 0.0
inputContinue = True

while boolContinue == True:
	strMetricSys = input("Enter Imperial (i) or Metric (m) data? ")
	if strMetricSys.lower() == "i" or strMetricSys.lower() == "m":

		#input weight and height
		if strMetricSys.lower() == "i":
			fWeight = float(input("Enter weight in pounds: ")) * 0.453592
			iFeet = int(input("Enter height:\nFeet: "))
			iInches = int(input("Inches: "))
			fHeight = (iFeet * 12 + iInches) * 0.0254
		else :
			fWeight = float(input("Enter weight in kilograms: "))
			fHeight = float(input("Enter height in centimeters: "))

		# calculate BMI
		fBMI = fWeight / pow(fHeight, 2)

		# check the category
		if fBMI < 16.0:
			print("You BMI = " + str(fBMI) +
				"\nSeverely	Underweight catergory!")
		elif 16 <= fBMI < 18.5:
			print("You BMI = " + str(fBMI) +
				"\nUnderweight catergory!")
		elif 18.5 <= fBMI < 25:
			print("You BMI = " + str(fBMI) +
				"\nNormal catergory!")
		elif 25 <= fBMI < 30:
			print("You BMI = " + str(fBMI) +
				"\nOverweight catergory!")
		elif 30 <= fBMI < 35:
			print("You BMI = " + str(fBMI) +
				"\nObese Class I catergory!")
		elif 35 <= fBMI < 40:
			print("You BMI = " + str(fBMI) +
				"\nObese Class II catergory!")
		else :
			print("You BMI = " + str(fBMI) +
				"\nObese Class III catergory!")

		# next input
		inputContinue = True
		while inputContinue == True:
			strContinue = input("Do you want to re-calculate? (Y/N) ")
			inputContinue = False

			if strContinue.lower() == 'y':
				boolContinue = True
				print ("\n\n")
			elif strContinue.lower() == 'n':
				boolContinue = False
				print ("Thank you for using BMI calculator!")
			else :
				inputContinue = True
	else :
		print("Incorrect input!")