class Orbits(object):
	def __init__(self, data, parent = None):
		self.parent = parent
		self.data = data
		
	def orbitChain(self) -> list:
		chain = []
		current_planet = self.parent
		while current_planet != None:
			chain.append(current_planet)
			current_planet = current_planet.parent
		return chain
	
	def countOrbits(self):
		return len(self.orbitChain())
				
		

with open('D:\Projects\AdventOfCode\day6-1.txt', 'r') as fp:
	line = fp.readlines()
	fp.close()
	orbits = dict()
	#print(line)
	for orb in line:
		#print(orb)
		p1 = orb.split(')')[0]
		p2 = orb.split(')')[1]
		p2 = p2.rstrip("\n\r")
		if p1 not in orbits:
			orbits[p1] = Orbits(p1)
		if p2 not in orbits:
			orbits[p2] = Orbits(p2)
		orbits[p2].parent = orbits[p1]
		print(p2 + " is a child of " + p1)
	print(sum((o.countOrbits() for o in orbits.values())))
	#for key in orbits["SAN"]:
	#	print(key)
	chain_SAN = orbits["SAN"].orbitChain()
	chain_YOU = orbits["YOU"].orbitChain()
	for parent in chain_SAN:
		if parent in chain_YOU:
			com_parent = parent
			break
	print(com_parent.data)
	orbS = 0
	for parent in chain_SAN:
		if parent == com_parent:
			break
		else:
			orbS += 1
	orbY = 0
	for parent in chain_YOU:
		if parent == com_parent:
			break
		else:
			orbY += 1
	print(orbS)
	print(orbY)
	print(orbits["SAN"].data)
	print(orbits["SAN"].parent.data)
	#print(len(orbits["SAN"].orbitChain))
			
		