with open("input.txt", "r") as f:
	input = f.readlines()

elves = []
x = 0
for i in range(len(input)):
	amount = input[i].replace("\n", "")
	if amount == "":
		x += 1
	else:
		if(x + 1 > len(elves)):
			elves.append(0)
		elves[x] += int(amount)

elves.sort(reverse=True)
print(elves[0] + elves[1] + elves[2])