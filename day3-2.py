import sys

trees1 = 0
trees2 = 0
trees3 = 0
trees4 = 0
trees5 = 0

currentX1 = 0
currentX2 = 0
currentX3 = 0
currentX4 = 0
currentY = 0

with open("day3.txt") as fp:
 	for line in fp:
 		if (line[currentX1] == "#"):
 			trees1 += 1
 		currentX1 = (currentX1 + 1) % (len(line)-1)

 		if (line[currentX2] == "#"):
 			trees2 += 1
 		currentX2 = (currentX2 + 3) % (len(line)-1)

 		if (line[currentX3] == "#"):
 			trees3 += 1
 		currentX3 = (currentX3 + 5) % (len(line)-1)

 		if (line[currentX4] == "#"):
 			trees4 += 1
 		currentX4 = (currentX4 + 7) % (len(line)-1)

 		if (currentY % 2 == 0):
 			if (line[currentX1] == "#"):
 				trees5 += 1
 		currentY += 1 
			
res = trees1 * trees2 * trees3 * trees4 * trees5
print(res)