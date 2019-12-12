import math
xLen = 0
yLen = 0
field = []
newField = []
totalAsteroids = 0

def closestAsteroid(x,y,angle):
	angleDistance = None
	distance = None
	coor = []
	newAngle = None
	print(angle)
	for rCount, row in enumerate(newField):
		for cCount, column in enumerate(row):
			#print(rCount)
			#print(cCount)
			if not column == '.':
				if float(column) >= angle:
					if angleDistance == None or float(column) - angle < angleDistance:
						angleDistance = float(column) - angle
						if distance == None or distance > abs([column-y]) + abs([row-x]):
							distance = abs(cCount-y) + abs(rCount-x)
							print("NEW COOR")
							coor = [cCount,rCount]
							newAngle = float(column)
	print(coor)
	newField[coor[1]][coor[0]] = '.'
	return coor, newAngle

def laser(x,y):
	print("LASER")
	print(totalAsteroids)
	#print(newField)
	angle = 90
	for count in range(totalAsteroids-1):
		asteroid, angle = closestAsteroid(x,y,angle)
		angle += 0.00000000000001
		print("ASTEROID #" + str(count + 1) + " at coor " + str(asteroid) + " destroyed")
		

def asteroidField(x,y):
	angles = []
	for rowL in range(x,-1,-1):
		for column in range(columnN):
			#print(str(xL) + " " + str(yR))
			#print("LEFT SIDE: " + str(rowL) + " " + str(column) + " " + str(field[column][rowL]), end = '')
			#print(field[xL][yR])
			if field[column][rowL] == "#" and not ((rowL == x) and (column == y)):
				angleString = ""
				if column < y:
					angleString = str(math.degrees(math.atan2(abs(rowL-x),abs(column-y))))
				elif column > y:
					angleString += str(270 + math.degrees(math.atan2(abs(rowL-x),abs(column-y))))
				if rowL-x == 0:
					if column-y > 0:
						angleString = "270"
					elif column-y < 0:
						angleString = "90"
				elif column-y == 0:
					if rowL-x > 0:
						angleString = "180"
					elif rowL-x < 0:
						angleString = "0"
					#print("PRE-TAN: " + str(column) + " " + str(rowL))
					#print("TAN: " + str(rowL-x) + " " + str(column-y))
					#print(angleString)
				#if not angleString in angles:
				angles.append(angleString)
				newField[column][rowL] = angleString
					#print(angleString)
					#print("COUNT")
	for rowR in range(x,rowN):
		for column in range(columnN):
			
			#print(field[xR][yR])
			#print("RIGHT SIDE: " + str(rowR) + " " + str(column) + " " + str(field[column][rowR]), end = '')
			if field[column][rowR] == "#" and not ((rowR == x) and (column == y)):
				#print(str(xR) + " " + str(yR) + " ", end = '')
				angleString = ""
				#if rowR != x:
					#angleString += "R"
				if column < y:
					angleString = str(90 + math.degrees(math.atan2(abs(rowR-x),abs(column-y))))
				elif column > y:
					angleString += str(180 + math.degrees(math.atan2(abs(rowR-x),abs(column-y))))
				if rowR-x == 0:
					if column-y > 0:
						angleString = "270"
					elif column-y < 0:
						angleString = "90"
				elif column-y == 0:
					if rowR-x > 0:
						angleString = "180"
					elif rowR-x < 0:
						angleString = "0"
				
					#print("PRE-TAN: " + str(column) + " " + str(rowR))
					#print("TAN: " + str(rowR-x) + " " + str(column-y))
					#print(angleString)
				#if not angleString in angles:
				angles.append(angleString)
				newField[column][rowL] = angleString
					#print(angleString)
					#print("COUNT")
	#print(angles)
	return newField

def countAsteroids(x,y):
	angles = []
	for rowL in range(x,-1,-1):
		for column in range(columnN):
			#print(str(xL) + " " + str(yR))
			#print("LEFT SIDE: " + str(rowL) + " " + str(column) + " " + str(field[column][rowL]), end = '')
			#print(field[xL][yR])
			if field[column][rowL] == "#" and not ((rowL == x) and (column == y)):
				angleString = ""
				if column < y:
					angleString = str(math.degrees(math.atan2(abs(rowL-x),abs(column-y))))
				elif column > y:
					angleString += str(270 + math.degrees(math.atan2(abs(rowL-x),abs(column-y))))
				if rowL-x == 0:
					if column-y > 0:
						angleString = "270"
					elif column-y < 0:
						angleString = "90"
				elif column-y == 0:
					if rowL-x > 0:
						angleString = "180"
					elif rowL-x < 0:
						angleString = "0"
					#print("PRE-TAN: " + str(column) + " " + str(rowL))
					#print("TAN: " + str(rowL-x) + " " + str(column-y))
					#print(angleString)
				if not angleString in angles:
					angles.append(angleString)
					#print(angleString)
					#print("COUNT")
	for rowR in range(x,rowN):
		for column in range(columnN):
			
			#print(field[xR][yR])
			#print("RIGHT SIDE: " + str(rowR) + " " + str(column) + " " + str(field[column][rowR]), end = '')
			if field[column][rowR] == "#" and not ((rowR == x) and (column == y)):
				#print(str(xR) + " " + str(yR) + " ", end = '')
				angleString = ""
				#if rowR != x:
					#angleString += "R"
				if column < y:
					angleString = str(90 + math.degrees(math.atan2(abs(rowR-x),abs(column-y))))
				elif column > y:
					angleString += str(180 + math.degrees(math.atan2(abs(rowR-x),abs(column-y))))
				if rowR-x == 0:
					if column-y > 0:
						angleString = "270"
					elif column-y < 0:
						angleString = "90"
				elif column-y == 0:
					if rowR-x > 0:
						angleString = "180"
					elif rowR-x < 0:
						angleString = "0"
				
					#print("PRE-TAN: " + str(column) + " " + str(rowR))
					#print("TAN: " + str(rowR-x) + " " + str(column-y))
					#print(angleString)
				if not angleString in angles:
					angles.append(angleString)
					#print(angleString)
					#print("COUNT")
	print(angles)
	return len(angles)

with open('D:\Projects\AdventOfCode\day10-1.txt', 'r') as fp:
	read = fp.read().splitlines()
	rowN = len(read)
	columnN = len(read[0])
	for x in range(xLen):
		print(x)
	print("ROWS: " + str(rowN))
	print("COLUMNS: " + str(columnN))
	field = [[x for x in line] for line in read]
	for row in field:
		totalAsteroids += row.count('#')
	#print(field)
	highestCount = 0
	for x in range(rowN):
		print(field[x])
	for x in range(rowN):
		#print(field[x])
		for y in range(columnN):
			if field[x][y] == "#":
				asteroidCount = countAsteroids(y,x)
				#asteroidCount = 0
				print("X: " + str(x) + " Y: " + str(y) + " Asteroid Count: " + str(asteroidCount))
				if highestCount < asteroidCount:
					highestCount = asteroidCount
	
	asteroidCount = countAsteroids(31,20)
	newField = field
	newField = asteroidField(x,y)
	print(newField)
	print(asteroidCount)
	print(highestCount)
	laser(31,20)
	#print(field[0][0])
	#print(field[1][0])
	#print(field[0][1])
	#print(field[3][2])
	