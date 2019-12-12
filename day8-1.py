import math

with open('D:\Projects\AdventOfCode\day8-1.txt', 'r') as fp:
	line = fp.readline()
	width = 25
	height = 6
	laylen = math.floor(len(line)/ (width*height))
	#print(laylen)
	layers = []
	for lay in range(laylen):
		onelayer = []
		for h in range(height):
			onelayer.append(line[(height*width*lay) + (h*width):(height*width*lay+width) + (h*width)])
		layers.append(onelayer)
	mostZeroLayer = [None, None, None, None]
	for count, layer in enumerate(layers):
		layerZeroCount = 0
		layerOneCount = 0
		layerTwoCount = 0
		for digits in layer:
			#print(digits)
			layerZeroCount += digits.count('0')
			layerOneCount += digits.count('1')
			layerTwoCount += digits.count('2')
		if (mostZeroLayer[0] == None) or (layerZeroCount < mostZeroLayer[1]):
			mostZeroLayer = [count, layerZeroCount, layerOneCount, layerTwoCount]
			#print("LOWEST")
	picture = layers[0]
	for layer in layers:
		#print(layer)
		for row in range(height):
			newRow = ""
			for digit in range(width):
				if int(picture[row][digit]) == 2:
					picture[row] = picture[row][0:digit] + layer[row][digit] + picture[row][digit+1:]
					#print(layer[row][digit])
					#newRow += layer[row][digit]
				#else:
					#newRow += picture[row][digit]
			#picture[row] = newRow
	for row in picture:
		#print(row)
		for digit in row:
			#print(digit)
			if int(digit)==0:
				print(" ", end = '')
			elif int(digit)==1:
				print("#", end = '')
		print("\n", end = '')
	#print(mostZeroLayer)
	#print(mostZeroLayer[2] * mostZeroLayer[3])