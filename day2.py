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
		frequency = rule.split(" ")[0]
		ruleLetter = rule.split(" ")[1]
		minumum = int(frequency.split("-")[0])
		maximum = int(frequency.split("-")[1])

		characterCount = 0
		for character in word:
			if (character == ruleLetter):
				characterCount += 1
		if (characterCount >= minumum and characterCount <= maximum):
			count += 1
			
print(count)