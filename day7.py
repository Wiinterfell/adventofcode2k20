import sys

# idea: map with colour as key and table of bags as value
# 1. build the map
# 2. Go through map

def findShinyGold(hierarchy, bag):
	if (bag == "shiny gold"):
		return True
	else:
		for newBag in hierarchy[bag]:
			if findShinyGold(hierarchy, newBag):
				return True
		return False


hierarchy = {}

with open("day7.txt") as fp:
 	for line in fp:
 		words = line.strip().split(" ")
 		parent = words[0] + " " + words[1]
 		children = []
 		i = 5 #first child starts
 		while (i < len(words)):
 			child = words[i] + " " + words[i+1]
 			if child != "other bags.":
	 			children.append(child)
 			i += 4
 		hierarchy[parent] = children

sum = 0
for key in hierarchy.keys():
	if findShinyGold(hierarchy, key):
		sum += 1

print(sum - 1)