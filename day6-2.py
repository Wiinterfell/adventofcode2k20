import sys

totalCount = 0
commonSet = set()
justReset = True

with open("day6.txt") as fp:
 	for line in fp:
 		if (line.strip() == ""):
 			#reset group
 			totalCount += len(commonSet)
 			commonSet = set()
 			justReset = True
 		else:
 			if justReset:
	 			# initialize with every answer
	 			for letter in line.strip():
	 				commonSet.add(letter)
	 			justReset = False
	 		else:
	 			lineSet = set(line.strip())
	 			copy = commonSet.copy()
	 			for letter in copy:
	 				if not(letter in lineSet):
	 					commonSet.remove(letter)

totalCount += len(commonSet)

print(totalCount)