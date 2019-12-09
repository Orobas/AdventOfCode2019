import collections
def constructWire(wiring):
	wire = [[0,0]]
	for instruction in wiring:
		if instruction[0] == 'U':
			direction = [0,1]
		elif instruction[0] == 'D':
			direction = [0,-1]
		elif instruction[0] == 'L':
			direction = [-1,0]
		elif instruction[0] == 'R':
			direction = [1,0]
		for x in range(int(instruction[1:])):
			wire.append([wire[-1][0] + direction[0],wire[-1][1] + direction[1]])
	return wire

with open('D:\Projects\AdventOfCode\day3-1.txt', 'r') as fp:
	line1 = fp.readline()
	line2 = fp.readline()
	wiring1 = line1.split(',')
	wiring2 = line2.split(',')
	wire1 = constructWire(wiring1)
	wire2 = constructWire(wiring2)
	overlap = [[0,0,0]]
	for point in wire1:
		if point != [0,0]:
			if point in wire2:
				overlap.append([point[0],point[1],wire1.index(point) + wire2.index(point)])
				print("OVERLAP" + str(point) + "Distance = " + str(wire1.index(point)) + " & " + str(wire2.index(point)))
				#overlap.append(point)
	manDistance = 0
	for point in overlap:
		distance = point[2]
		if distance != 0:
			if manDistance == 0 or distance < manDistance:
				manDistance = distance
	print(manDistance)
	#print(wire1)
	#print(wire1[0])