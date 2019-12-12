import re
import math
moonInfo = []
totalMoons = 0
moonHistory = []

def lcm(X,Y,Z):
	lcm_X = 0
	lcm_Y = 0
	lcm_Z = 0
	for ind in range(totalMoons-1):
		if lcm_X == 0:
			lcm_X = X[ind] * X[ind+1] // math.gcd(X[ind],X[ind+1])
		else:
			lcm_X = lcm_X * X[ind+1] // math.gcd(lcm_X,X[ind+1])
		if lcm_Y == 0:
			lcm_Y = Y[ind] * Y[ind+1] // math.gcd(Y[ind],Y[ind+1])
		else:
			lcm_Y = lcm_Y * Y[ind+1] // math.gcd(lcm_Y,Y[ind+1])
		if lcm_Z == 0:
			lcm_Z = Z[ind] * Z[ind+1] // math.gcd(Z[ind],Z[ind+1])
		else:
			lcm_Z = lcm_Z * Z[ind+1] // math.gcd(lcm_Z,Z[ind+1])
	lcm_xy = (lcm_X * lcm_Y) // math.gcd(lcm_X,lcm_Y)
	lcm_xyz = (lcm_xy * lcm_Z) // math.gcd(lcm_xy, lcm_Z)
	return lcm_xyz

def historyRepeatVelocity(stepNum, xRepeat, yRepeat, zRepeat):
	stepNumT = 0
	moon = moonHistory[0]
	moon = moon.replace('[','')
	moon = moon.replace(']','')
	moon = moon.replace(' ','')
	moonI = moon.split(',')
	for moonN in range(totalMoons):
		if stepNum == 6:
			print("moonInfo " + str(moonInfo[moonN][0]) + " moonI " + str(moonI[moonN*6]) + " moonInfo " + str(moonInfo[moonN][3]) + " moonI " + str(moonI[moonN*6+3]))
		if str(moonInfo[moonN][0]) == moonI[moonN*6] and str(moonInfo[moonN][3]) == moonI[moonN*6+3] and stepNum != 0 and xRepeat[moonN] == 0:
		#if str(moonInfo[moonN][3]) == moonI[moonN*6+3]:
			print("XMATCH")
			print("mooninfo[moonN][0] " + str(moonInfo[moonN][0]) + " moonHistory " + str(moonI[moonN*6+0]) + " mooninfo[moonN][3] " + str(moonInfo[moonN][3]) + " moonHistory " + str(moonI[moonN*6+3]))
			xRepeat[moonN] = stepNum
		if str(moonInfo[moonN][1]) == moonI[moonN*6+1] and str(moonInfo[moonN][4]) == moonI[moonN*6+4] and stepNum != 0 and yRepeat[moonN] == 0:
		#if str(moonInfo[moonN][4]) == moonI[moonN*6+4]:
			print("YMATCH")
			print("mooninfo[moonN][1] " + str(moonInfo[moonN][1]) + " moonHistory " + str(moonI[moonN*6+1]) + " mooninfo[moonN][4] " + str(moonInfo[moonN][4]) + " moonHistory " + str(moonI[moonN*6+4]))
			yRepeat[moonN] = stepNum
		#if str(moonInfo[moonN][5]) == moonI[moonN*6+5]:
		if str(moonInfo[moonN][2]) == moonI[moonN*6+2] and str(moonInfo[moonN][5]) == moonI[moonN*6+5] and stepNum != 0 and zRepeat[moonN] == 0:
			print("ZMATCH")
			print("mooninfo[moonN][2] " + str(moonInfo[moonN][2]) + " moonHistory " + str(moonI[moonN*6+2]) + " mooninfo[moonN][5] " + str(moonInfo[moonN][5]) + " moonHistory " + str(moonI[moonN*6+5]))
			zRepeat[moonN] = stepNum
	
	#for moon in moonHistory:
		
		#moon = moon.replace('[','')
		#moon = moon.replace(']','')
		#moon = moon.replace(' ','')
		#moonI = moon.split(',')
		#if stepNum == 2772 and stepNumT == 0: print("COMPARING")
		#if stepNum == 2772 and stepNumT == 0: print(moonInfo[0])
		#if stepNum == 2772 and stepNumT == 0: print("MOONINFO[0] " + str(moonInfo[0][0]) + " AND moonHistory " + str(moonI[0]))
		#if stepNum == 2772 and stepNumT == 0: print("MOONINFO[3] " + str(moonInfo[0][3]) + " AND moonHistory " + str(moonI[3]))
		#if stepNum == 2772 and stepNumT == 0: print(moonI)
		#if str(moonInfo[0][0]) == moonI[0] and stepNumT == 0: print("X MATCH")
		#if str(moonInfo[0][3]) == moonI[3]: print("XV MATCH")
		#if str(moonInfo[0][0]) == moonI[0] and str(moonInfo[0][3]) == moonI[3] and stepNum != 0 and xRepeat == 0:
		#	print("XMATCH")
		#	print("mooninfo[0][0] " + str(moonInfo[0][0]) + " moonHistory " + str(moonI[0]) + " mooninfo[0][3] " + str(moonInfo[0][3]) + " moonHistory " + str(moonI[3]))
		#	xRepeat = stepNum
		#	print(xRepeat)
		#if str(moonInfo[0][1]) == moonI[1] and str(moonInfo[0][4]) == moonI[4] and stepNum != 0 and yRepeat == 0:
		#	print("YMATCH")
		#	print("mooninfo[0][1] " + str(moonInfo[0][1]) + " moonHistory " + str(moonI[1]) + " mooninfo[0][4] " + str(moonInfo[0][4]) + " moonHistory " + str(moonI[4]))
		#	yRepeat = stepNum
		#	print(yRepeat)
		#if str(moonInfo[0][2]) == moonI[2] and str(moonInfo[0][5]) == moonI[5] and stepNum != 0 and zRepeat == 0:
		#	print("ZMATCH")
		#	print("mooninfo[0][2] " + str(moonInfo[0][2]) + " moonHistory " + str(moonI[2]) + " mooninfo[0][5] " + str(moonInfo[0][5]) + " moonHistory " + str(moonI[5]))
		#	zRepeat = stepNum
		#	print(zRepeat)
		#stepNumT += 1
	return xRepeat, yRepeat, zRepeat
	#return xRepeat

def historyRepeat():
	index = -1
	#print("HISTORY:")
	#print(moonInfo)
	#print(moonHistory)
	if str(moonInfo) in moonHistory:
		index = moonHistory.index(str(moonInfo))
	return index

def calculateEnergy():
	totalE = 0
	for moonN in range(totalMoons):
		potentialE = abs(moonInfo[moonN][0]) + abs(moonInfo[moonN][1]) + abs(moonInfo[moonN][2])
		kineticE = abs(moonInfo[moonN][3]) + abs(moonInfo[moonN][4]) + abs(moonInfo[moonN][5])
		totalE += potentialE * kineticE
	return totalE

def moveMoons():
	for moonN in range(totalMoons):
		moonInfo[moonN][0] += moonInfo[moonN][3]
		moonInfo[moonN][1] += moonInfo[moonN][4]
		moonInfo[moonN][2] += moonInfo[moonN][5]

def calculateVelocity():
	for curMoon in range(totalMoons):
		xVel = moonInfo[curMoon][3]
		yVel = moonInfo[curMoon][4]
		zVel = moonInfo[curMoon][5]
		for moonN in range(totalMoons):
			if moonInfo[curMoon][0] < moonInfo[moonN][0]:
				xVel += 1
			elif moonInfo[curMoon][0] > moonInfo[moonN][0]:
				xVel += -1
			if moonInfo[curMoon][1] < moonInfo[moonN][1]:
				yVel += 1
			elif moonInfo[curMoon][1] > moonInfo[moonN][1]:
				yVel += -1
			if moonInfo[curMoon][2] < moonInfo[moonN][2]:
				zVel += 1
			elif moonInfo[curMoon][2] > moonInfo[moonN][2]:
				zVel += -1
		moonInfo[curMoon][3] = xVel
		moonInfo[curMoon][4] = yVel
		moonInfo[curMoon][5] = zVel

with open('D:\Projects\AdventOfCode\day12-test.txt', 'r') as fp:
	moons = fp.readlines()
	totalMoons = len(moons)
	steps = 1000
	for moon in moons:
		moon = moon.replace('>', '')
		moon = moon.rstrip("\n\r")
		input = moon.split(",")
		xcoor = int(input[0].split("=")[1])
		ycoor = int(input[1].split("=")[1])
		zcoor = int(input[2].split("=")[1])
		moonInfo.append([xcoor, ycoor, zcoor, 0, 0, 0])
	print(totalMoons)
	print("Step 0")
	print(moonInfo)
	stepN = 0
	moonHistory.append(str(moonInfo))
	#for x in range(0,steps):
	repeat = False
	repeatN = -1
	rX = [0,0,0,0]
	rY = [0,0,0,0]
	rZ = [0,0,0,0]
	while(repeat == False):
		stepN += 1
		calculateVelocity()
		moveMoons()
		#if stepN % 100000 == 0: print(str(stepN) + " number of steps")
		print(str(stepN) + " number of steps")
		print(moonInfo)
		#print("MOONHISTORY: " + str(moonHistory))
		#repeatN = historyRepeat()
		rX, rY, rZ = historyRepeatVelocity(stepN, rX, rY, rZ)
		if not (0 in rX) and not (0 in rY) and not (0 in rZ):
		#rX = historyRepeatVelocity(stepN)
		#if rX != 0:
			print("VELOCITY REPEATS")
			print(rX)
			print(rY)
			print(rZ)
			#arr = [rX,rY,rZ]
			print(lcm(rX,rY,rZ))
			
			repeat = True
		#historyRepeatVelocity()
		if repeatN != -1:
			repeat = True
			print("REPEAT AT " + str(repeatN) + " and " + str(stepN))
		moonHistory.append(str(moonInfo))
	print(calculateEnergy())
	#print(moonHistory)
	