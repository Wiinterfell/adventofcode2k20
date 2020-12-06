import sys

numbers = set()
with open("day1.txt") as fp:
 	for line in fp:
		expense = int(line)
		
		complementary = 2020 - expense
		if (complementary in numbers):
			print(complementary * expense)
			break
		if not(expense in numbers):
			numbers.add(expense)
			
	print(numbers)