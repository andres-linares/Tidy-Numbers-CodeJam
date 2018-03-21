# -*- coding: utf-8 -*-

def main():
	file = open("B-large-practice.in", "r")
	outputFile = open("output2.txt", "w")
	testCases = int(file.readline())
	for x in range(0, testCases):
		number = file.readline().split()
		solution = solve(number[0])
		output = "Case #{0}: {1}\n".format(x+1, solution)
		outputFile.write(output)
	outputFile.close()

def solve(number):
	size = len(number)

	if size == 1:
		return number

	newNumber = ""
	panicFlag = False
	beautifulFlag = False
	for x in range(0, size - 1):
		if panicFlag == False:
			numberA = int(number[x])
			numberB = int(number[x + 1])
			if numberA > numberB:
				numberA -= 1
				panicFlag = True
				beautifulFlag = True
			if x != 0:
				newNumber += str(numberA)
			else:
				if numberA != 0:
					newNumber += str(numberA)
		else:
			newNumber += '9'
	if panicFlag == False:
		newNumber += number[len(number) - 1]
	else:
		newNumber += '9'

	if beautifulFlag:
		return solve(newNumber)
	else:
		return newNumber



if __name__ == "__main__":
	main()