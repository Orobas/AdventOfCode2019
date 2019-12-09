with open('D:\Projects\AdventOfCode\day2-1.txt', 'r') as fp:
	total = 0
	line = fp.readline()
	pos = line.split(',')
	opnumber = 0
	solution=False
	for x in range(100):
		if solution:
			break
		for y in range(100):
			if solution:
				break
			opnumber = 0
			pos = line.split(',')
			pos[1] = x
			pos[2] = y
			print("X: " + str(x))
			print("Y: " + str(y))
			run=True
			while(run):
				opcode=int(pos[opnumber*4])
				num1Pos=int(pos[opnumber*4 + 1])
				num1=int(pos[num1Pos])
				num2Pos=int(pos[opnumber*4 + 2])
				num2=int(pos[num2Pos])
				outputPos=int(pos[opnumber*4 + 3])
				if opcode==99:
					run=False
					#print("OP 99 FOUND")
					continue
				elif opcode==1:
					output = num1+num2
					#print("OP 1, add pos " + str(num1Pos) + " and pos" + str(num2Pos) + "and save at pos " + str(outputPos))
					#print(str(num1) + " + " + str(num2) + " = " + str(output))
				elif opcode==2:
					output = num1*num2
					#print("OP 1, multiply pos " + str(num1Pos) + " and pos" + str(num2Pos) + "and save at pos " + str(outputPos))
					#print(str(num1) + " X " + str(num2) + " = " + str(output))
				else: 
					print("ERROR, UNKNOWN OPCODE")
					run=False
					continue
				pos[outputPos] = output
				opnumber += 1
			if pos[0] == 19690720:
				solution=True
				print("NOUN: " + str(x))
				print("VERB: " + str(y))
				