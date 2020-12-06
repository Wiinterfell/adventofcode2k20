import sys

currentX = 0
trees = 0
with open("day3.txt") as fp:
 	for line in fp:
 		if (line[currentX] == "#"):
 			trees += 1
 		currentX = (currentX + 3) % (len(line)-1)
			
print(trees)