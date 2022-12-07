# Round 1
# with open("test.txt", "r") as f:
# 	input = f.readlines()

# groups = []

# for line in input:
# 	line = line.replace("\n", "")
# 	group = line.split(",")
# 	elve1 = group[0].split("-")
# 	elve2 = group[1].split("-")

# 	elve1Area = []
# 	for i in range(int(elve1[0]), int(elve1[1]) + 1):
# 		elve1Area.append(str(i))

# 	elve2Area = []
# 	for i in range(int(elve2[0]), int(elve2[1]) + 1):
# 		elve2Area.append(str(i))

# 	groups.append([elve1Area, elve2Area])

# count = 0
# for group in groups:
# 	if all(elem in group[0]  for elem in group[1]) or all(elem in group[1]  for elem in group[0]):
# 		count += 1

# print(count)

#Round 2
with open("input.txt", "r") as f:
	input = f.readlines()

groups = []

for line in input:
	line = line.replace("\n", "")
	group = line.split(",")
	elve1 = group[0].split("-")
	elve2 = group[1].split("-")

	elve1Area = []
	for i in range(int(elve1[0]), int(elve1[1]) + 1):
		elve1Area.append(str(i))

	elve2Area = []
	for i in range(int(elve2[0]), int(elve2[1]) + 1):
		elve2Area.append(str(i))

	groups.append([elve1Area, elve2Area])

count = 0
for group in groups:
	for num in group[0]:
		if num in group[1]:
			count += 1
			break

print(count)
