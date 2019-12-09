import math

def getFuel(mass):
	fuel = math.floor(mass/3) - 2
	if fuel > 0:
		return fuel + getFuel(fuel)
	else:
		return 0
	
with open('D:\Projects\AdventOfCode\day1-1.txt', 'r') as fp:
	total = 0
	for cnt, line in enumerate(fp):
		total += getFuel(int(line))
	print(total)
