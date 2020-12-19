import sys

def findShinyGold(hierarchy, bag):
	sum = 0
	for newBag in hierarchy[bag]:
		number = findShinyGold(hierarchy, newBag[0])
		sum += newBag[1] * (number + 1)
	return sum


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
 				count = int(words[i-1])
	 			children.append([child, count])
 			i += 4
 		hierarchy[parent] = children

goldCount = findShinyGold(hierarchy, "shiny gold")

print(goldCount)