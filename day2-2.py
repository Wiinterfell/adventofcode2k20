import sys

"""
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
"""

count = 0
with open("day2.txt") as fp:
 	for line in fp:
		rule = line.split(":")[0]
		word = line.split(":")[1]
		positions = rule.split(" ")[0]
		ruleLetter = rule.split(" ")[1]
		first = int(positions.split("-")[0])
		second = int(positions.split("-")[1])

		if((word[first] == ruleLetter) ^ (word[second] == ruleLetter)):		
			count += 1
			
print(count)