import sys

expenseList = []
with open("day1.txt") as fp:
 	for line in fp:
		expenseList.append(int(line))
		
for i in range(0, len(expenseList)):
	for j in range(i, len(expenseList)):
		for k in range(j, len(expenseList)):
			if (expenseList[i] + expenseList[j] + expenseList[k] == 2020):
				print(expenseList[i] * expenseList[j] * expenseList[k])
				break