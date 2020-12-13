import sys

totalCount = 0
groupSet = set()

with open("day6.txt") as fp:
 	for line in fp:
 		if (line.strip() == ""):
 			#reset group
 			totalCount += len(groupSet)
 			groupSet = set()
 		else:
 			for letter in line.strip():
 				groupSet.add(letter)

totalCount += len(groupSet)

print(totalCount)