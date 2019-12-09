def checkSequence(password, index):
	sequenceCount = 1
	for x in range(index+1,len(password)):
		if password[index] == password[x]:
			sequenceCount += 1
	for x in range(index-1, -1,-1):
		if password[index] == password[x]:
			sequenceCount += 1
	return sequenceCount

def checkPassword(password):
	sequence = False
	if len(password) != 6: 
		return False
	for x in range(len(password)-1):
		if int(password[x]) > int(password[x+1]):
			return False
		elif int(password[x]) == int(password[x+1]):
			if checkSequence(password,x) == 2:
				sequence = True
	return sequence

with open('D:\Projects\AdventOfCode\day4-1.txt', 'r') as fp:
	limit = fp.readline().split('-')
	min = int(limit[0])
	max = int(limit[1])
	passwordCount = 0
	for passw in range(min,max):
	#for passw in range(333333,340000):
		valid = checkPassword(str(passw))
		if valid:
			#print(passw)
			passwordCount += 1
	print(passwordCount)