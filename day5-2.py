import sys

seats = [False] * (128 * 8)

with open("day5.txt") as fp:
 	for line in fp:
 		rowCode = line.strip()[:7]
 		front = 0
 		back = 127
 		for letter in rowCode[:-1]:
 			middle = ((back - front) / 2) + front
 			if letter == "F":
 				back = middle
 			else:
 				front = middle + 1
 		if rowCode[-1] == "F":
 			row = front
 		else: 
 			row = back

 		columnCode = line.strip()[7:]
 		front = 0
 		back = 7
 		for letter in columnCode[:-1]:
 			middle = ((back - front) / 2) + front
 			if letter == "L":
 				back = middle
 			else:
 				front = middle + 1
 		if columnCode[-1] == "L":
 			column = front
 		else: 
 			column = back
		
		seatId = row * 8 + column
		seats[seatId] = True

for i in range(1, len(seats)-1):
	if (not(seats[i]) and seats[i-1] and seats[i+1]):
		print(i)