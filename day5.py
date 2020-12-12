import sys

highestSeatId = 0

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
 		column = front
		
		seatId = row * 8 + column
		if (seatId > highestSeatId):
			highestSeatId = seatId

print(highestSeatId)