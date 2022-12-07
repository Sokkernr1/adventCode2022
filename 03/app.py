# Round 1
# with open("input.txt", "r") as f:
# 	input = f.readlines()

# backpacks = []
# for i in range(len(input)):
	# backpacks.insert(i, [0, 0])
	# backpacks[i][0] = input[i].replace("\n", "")[slice(0, int(len(input[i]) / 2))]
	# backpacks[i][1] = input[i].replace("\n", "")[slice(int(len(input[i]) / 2), int(len(input[i])))]

# commonItem = []
# itemWorth = []
# for backpack in backpacks:
# 	found = False
# 	for letter in backpack[0]:
# 		for letter2 in backpack[1]:
# 			if letter == letter2:
# 				commonItem.append(letter)
# 				if(letter.isupper()):
# 					itemWorth.append(ord(letter) - 38)
# 				else:
# 					itemWorth.append(ord(letter) - 96)
# 				found = True
# 				break
# 		if found: break

# print(commonItem)
# print(itemWorth)
# print(sum(itemWorth))

# Round 2
with open("input.txt", "r") as f:
	input = f.readlines()

groups = []
for i in range(0, len(input), 3):
	groups.append([
		input[i], 
		input[i + 1], 
		input[i + 2]
	])

commonItem = []
itemWorth = []
for group in groups:
	for letter in group[0]:
		if letter in group[1] and letter in group[2]:
			commonItem.append(letter)
			if(letter.isupper()):
				itemWorth.append(ord(letter) - 38)
			else:
				itemWorth.append(ord(letter) - 96)
			break

print(commonItem)
print(itemWorth)
print(sum(itemWorth))