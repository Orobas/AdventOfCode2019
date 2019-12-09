import math
pos = ""

def op1(index,mode1,mode2):
	if mode1 == 1:
		num1 = int(pos[index + 1])
	else:
		num1Pos = int(pos[index + 1])
		num1 = int(pos[num1Pos])
	if mode2 == 1:
		num2 = int(pos[index+2])
	else:
		num2Pos = int(pos[index + 2])
		num2 = int(pos[num2Pos])
	outputPos = int(pos[index + 3])
	output = num1 + num2
	pos[outputPos] = output
	#print("OP1: num1: " + str(num1) + " num2: " + str(num2) + " outputPos: " + str(outputPos) + " output: " + str(output))
	return index+4

def op2(index,mode1,mode2):
	if mode1 == 1:
		num1 = int(pos[index + 1])
	else:
		num1Pos = int(pos[index + 1])
		num1 = int(pos[num1Pos])
	if mode2 == 1:
		num2 = int(pos[index + 2])
	else:
		num2Pos = int(pos[index + 2])
		num2 = int(pos[num2Pos])
	outputPos = int(pos[index + 3])
	output = num1 * num2
	pos[outputPos] = output
	#print("OP2: num1: " + str(num1) + " num2: " + str(num2) + " outputPos: " + str(outputPos) + " output: " + str(output))
	return index+4

def op3(index, input):
	num1Pos = int(pos[index + 1])
	pos[num1Pos] = input
	return index+2
	
def op4(index, mode1):
	if mode1 == 1:
		output = pos[index + 1]
	else:
		num1Pos = int(pos[index + 1])
		output = int(pos[num1Pos])
	return index+2, output

def op5(index, mode1, mode2):
	if mode1 == 1:
		num1 = int(pos[index + 1])
	else:
		num1Pos = int(pos[index + 1])
		num1 = int(pos[num1Pos])
	if num1 != 0:
		if mode2 == 1:
			num2 = int(pos[index + 2])
		else:
			num2Pos = int(pos[index + 2])
			num2 = int(pos[num2Pos])
		return num2
	return index + 3

def op6(index, mode1, mode2):
	if mode1 == 1:
		num1 = int(pos[index + 1])
	else:
		num1Pos = int(pos[index + 1])
		num1 = int(pos[num1Pos])
	if num1 == 0:
		if mode2 == 1:
			num2 = int(pos[index + 2])
		else:
			num2Pos = int(pos[index + 2])
			num2 = int(pos[num2Pos])
		#print("OP 6: num1: " + str(num1) + " num2: " + str(num2))
		return num2
	
	return index + 3

def op7(index, mode1, mode2):
	if mode1 == 1:
		num1 = int(pos[index + 1])
	else:
		num1Pos = int(pos[index + 1])
		num1 = int(pos[num1Pos])
	if mode2 == 1:
		num2 = int(pos[index + 2])
	else:
		num2Pos = int(pos[index + 2])
		num2 = int(pos[num2Pos])
	outputPos = int(pos[index + 3])
	if num1 < num2:
		pos[outputPos] = 1
	else:
		pos[outputPos] = 0
	#print("OP7: num1: " + str(num1) + " num2: " + str(num2) + " outputPos: " + str(outputPos))
	return index + 4

def op8(index, mode1, mode2):
	if mode1 == 1:
		num1 = int(pos[index + 1])
	else:
		num1Pos = int(pos[index + 1])
		num1 = int(pos[num1Pos])
	if mode2 == 1:
		num2 = int(pos[index + 2])
	else:
		num2Pos = int(pos[index + 2])
		num2 = int(pos[num2Pos])
	outputPos = int(pos[index + 3])
	if num1 == num2:
		pos[outputPos] = 1
	else:
		pos[outputPos] = 0
	#print("OP8: num1: " + str(num1) + " num2: " + str(num2) + " outputPos: " + str(outputPos))
	return index + 4
	
with open('D:\Projects\AdventOfCode\day5-1.txt', 'r') as fp:
	input = 5
	total = 0
	line = fp.readline()
	pos = line.split(',')
	opnumber = 0
	opN = 0
	index = 0
	run=True
	while(run):
		opcodeFull=int(pos[opnumber])
		opcode = opcodeFull % 100
		mode1 = math.floor(opcodeFull / 100) % 10 
		mode2 = math.floor(opcodeFull / 1000) % 10
		mode3 = math.floor(opcodeFull / 10000) % 10
		#print(opnumber)
		#print(pos)
		if opcode == 99:
			run=False
			continue
		elif opcode == 1:
			#print("OPNUM " + str(opN) + " OPCODE1: Mode1: " + str(mode1) + " Mode2: " + str(mode2))
			opnumber = op1(opnumber, mode1, mode2)
		elif opcode == 2:
			#print("OPNUM " + str(opN) + " OPCODE2: Mode1: " + str(mode1) + " Mode2: " + str(mode2))
			opnumber = op2(opnumber, mode1, mode2)
		elif opcode == 3:
			#print("OPNUM " + str(opN) + " OPCODE3: Input: " + str(input))
			opnumber = op3(opnumber, input)
		elif opcode == 4:
			opnumber, output = op4(opnumber, mode1)
			print(str(output) + " at OPNUMBER" + str(opN) + " From pos " + str(opnumber) + " Mode1: " + str(mode1))
		elif opcode == 5:
			#print("OPNUM " + str(opN) + " OPCODE5: Mode1: " + str(mode1) + " Mode2: " + str(mode2))
			opnumber = op5(opnumber, mode1, mode2)
		elif opcode == 6:
			#print("OPNUM " + str(opN) + " OPCODE6: Mode1: " + str(mode1) + " Mode2: " + str(mode2))
			opnumber = op6(opnumber, mode1, mode2)
		elif opcode == 7:
			#print("OPNUM " + str(opN) + " OPCODE7: Mode1: " + str(mode1) + " Mode2: " + str(mode2))
			opnumber = op7(opnumber, mode1, mode2)
		elif opcode == 8:
			#print("OPNUM " + str(opN) + " OPCODE8: Mode1: " + str(mode1) + " Mode2: " + str(mode2))
			opnumber = op8(opnumber, mode1, mode2)
		else: 
			print("ERROR, UNKNOWN OPCODE")
			run=False
			continue
		
		opN += 1

				