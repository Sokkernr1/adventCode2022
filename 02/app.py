# A, X = Rock (+1)
# B, Y = Paper (+2)
# C, Z = Scissor (+3)
# Win = +6 ; Draw = +3 ; Loss = +0

pointDict = {
	"A": 1,
	"B": 2,
	"C": 3,
	"X": 0,
	"Y": 3,
	"Z": 6
}

winDict = {
	1: 2,
	2: 3,
	3: 1
}

looseDict = {
	1: 3,
	2: 1,
	3: 2
}

with open("input.txt", "r") as f:
	input = f.readlines()

elveInput = []
playerInput = []
for line in input:
	elveInput.append(pointDict[line[0]])
	playerInput.append(pointDict[line[2]])

score = 0

# Round 1
# for i in range(len(playerInput)):
# 	x = elveInput[i] - playerInput[i]
# 	if(x == -1 or x == 2):
# 		score += 6
# 	elif(x == 0):
# 		score += 3
# 	score += playerInput[i]

# Round 2
for i in range(len(playerInput)):
	score += playerInput[i]
	if playerInput[i] == 6:
		score += winDict[elveInput[i]]
	elif playerInput[i] == 3:
		score += elveInput[i]
	else:
		score += looseDict[elveInput[i]]

print(score)
