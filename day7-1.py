import math
from itertools import permutations
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
	
with open('D:\Projects\AdventOfCode\day7-test.txt', 'r') as fp:
	phasePerm = permutations([5,6,7,8,9])
	phasePerm = [[9,8,7,6,5]]
	input = [0,0,0,0,0]
	output = [0,0,0,0,0]
	biggestOut = 0
	line = fp.readline()
	posOrig = line.split(',')
	opnumber = [0,0,0,0,0]
	opN = [0,0,0,0,0]
	amp = 0
	posA = [0,0,0,0,0]
	posA[0] = posOrig
	posA[1] = posOrig
	posA[2] = posOrig
	posA[3] = posOrig
	posA[4] = posOrig
	for phase in phasePerm:
		#input = 0
		for p in phase:
			pos = posA[amp]
			in1 = phasePerm[0][amp]
			in2 = input[amp]
			inputN = [0,0,0,0,0]
			#print("PHASE: " + str(p) + " INPUT: " + str(input))
			opN[amp] = 0
			index = 0
			run = [True, True, True, True, True]
			while(any(r == True for r in run)):
				print(str(run) + " and amp" + str(amp))
				if run[4] == False:
					run = [False, False, False, False, False]
				if run[amp]==False:
					amp += 1
					if amp == 5:
						amp = 0
				pos = posA[amp]
				#print(amp)
				#print(opnumber)
				#print(opnumber[amp])
				opcodeFull=int(pos[opnumber[amp]])
				opcode = opcodeFull % 100
				mode1 = math.floor(opcodeFull / 100) % 10 
				mode2 = math.floor(opcodeFull / 1000) % 10
				mode3 = math.floor(opcodeFull / 10000) % 10
				print(str(opcode) + " " + str(opnumber[amp]))
				#print(opnumber)
				#print(pos)
				if opcode == 99:
					run[amp]=False
					continue
				elif opcode == 1:
					#print("OPNUM " + str(opN) + " OPCODE1: Mode1: " + str(mode1) + " Mode2: " + str(mode2))
					opnumber[amp] = op1(opnumber[amp], mode1, mode2)
				elif opcode == 2:
					#print("OPNUM " + str(opN) + " OPCODE2: Mode1: " + str(mode1) + " Mode2: " + str(mode2))
					opnumber[amp] = op2(opnumber[amp], mode1, mode2)
				elif opcode == 3:
					#print("OPNUM " + str(opN) + " OPCODE3: Input: " + str(input))
					if inputN[amp] == 0:
						opnumber[amp] = op3(opnumber[amp], phasePerm[0][amp])
						inputN[amp] += 1
					else:
						opnumber[amp] = op3(opnumber[amp], input[amp])
				elif opcode == 4:
					opnumber[amp], ot = op4(opnumber[amp], mode1)
					print(str(ot) + " at OPNUMBER" + str(opN) + " From pos " + str(opnumber[amp]) + " AMP: " + str(amp) + " Mode1: " + str(mode1))
					print(pos[amp])
					#posA[amp] = pos
					amp += 1
					if amp == 5:
						amp = 0
					input[amp]=ot
				elif opcode == 5:
					print("OPNUM " + str(opN) + " OPCODE5: Mode1: " + str(mode1) + " Mode2: " + str(mode2) + "Index before: " + str(opnumber[amp]))
					opnumber[amp] = op5(opnumber[amp], mode1, mode2)
					print("INDEX AFTER: " + str(opnumber[amp]))
				elif opcode == 6:
					#print("OPNUM " + str(opN) + " OPCODE6: Mode1: " + str(mode1) + " Mode2: " + str(mode2))
					opnumber[amp] = op6(opnumber[amp], mode1, mode2)
				elif opcode == 7:
					#print("OPNUM " + str(opN) + " OPCODE7: Mode1: " + str(mode1) + " Mode2: " + str(mode2))
					opnumber[amp] = op7(opnumber[amp], mode1, mode2)
				elif opcode == 8:
					#print("OPNUM " + str(opN) + " OPCODE8: Mode1: " + str(mode1) + " Mode2: " + str(mode2))
					opnumber[amp] = op8(opnumber[amp], mode1, mode2)
				else: 
					print("ERROR, UNKNOWN OPCODE")
					run=False
					continue
				#print(pos)
				opN[amp] += 1
			if ot > biggestOut:
				biggestOut = ot
			#print(output)
			#input = output
	print(biggestOut)
				