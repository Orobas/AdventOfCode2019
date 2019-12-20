import math
cookbook = dict()
ingredientsReq = dict()

def readRecipeRequirements(ingredient, qReq):
	cookbookpage = cookbook[ingredient]
	cookbookpage = cookbookpage.split(",")
	quantity = cookbookpage[0]
	ore = 0
	recipeMult = math.ceil(int(qReq) / int(quantity))
	for piece in range(1,len(cookbookpage)):
		quan = cookbookpage[piece].strip("['] ").split(' ')[0]
		ing = cookbookpage[piece].strip("['] ").split(' ')[1]
		if ing == "ORE":
			return qReq
		if ing in ingredientsReq.keys():
			ingredientsReq[ing] += int(readRecipeRequirements(ing, quan)) * recipeMult
		else:
			ingredientsReq[ing] = int(readRecipeRequirements(ing, quan)) * recipeMult
	return qReq
	
			

def readRecipeOre():
	ingList = ingredientsReq
	print(ingredientsReq)
	oreAmount = 0
	for ing, amount in ingList.items():
		recipe = str(cookbook[ing])
		print(ing)
		print(recipe)
		makes = recipe.split(',')[0]
		rec = recipe.split(',')[1].strip("['] ")
		quan = rec.split(" ")[0]
		ore = rec.split(" ")[1]
		#print(ore)
		if ore == "ORE":
			print("ORE: " + str(quan) + " TIMES " + str(math.ceil(int(amount) / int(makes))))
			oreAmount += int(quan) * math.ceil(int(amount) / int(makes))
	return oreAmount
	
def reduceToBase():
	reducedcookbook = dict()
	baseElements = []
	for ing, amount in cookbook.items():
		if amount.split(" ")[2].strip("['] ") == "ORE":
			baseElements.append(ing)
	for ing, amount in cookbook.items():
		#print(amount)
		recipes = str(amount).split(',')
		#print(recipes)
		for recipe in recipes[1:]:
			#print(recipe)
			recIng = recipe.split(" ")[1].strip("['] ")
			recAmnt = recipe.split(" ")[0].strip("['] ")
			#print(recIng)
			reducedcookbook[ing] = recAmnt + " " + str(recIng)
	return reducedcookbook


with open('D:\Projects\AdventOfCode\day14-test.txt', 'r') as fp:
	lines = fp.readlines()
	#cookbook = dict()
	for recipe in lines:
		recipe = recipe.rstrip("\n\r")
		line = recipe.split(" => ")
		outputElement = line[1].split(" ")[1]
		outputQuantity = line[1].split(" ")[0]
		inputs = line[0].split(",")
		cookbookRecipe = outputQuantity
		for i in inputs:
			cookbookRecipe += ", " + i
		cookbook[outputElement] = outputQuantity + ", " + str(inputs)
		#print(inputs[1])
	print(cookbook)
	print(readRecipeRequirements("FUEL",1))
	#print(ingredientsReq)
	print(readRecipeOre())
	print(cookbook)
	print(reduceToBase())
	
	#totalMoons = len(moons)
	#steps = 1000