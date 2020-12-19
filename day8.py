import sys

instr = []

with open("day8.txt") as fp:
 	for line in fp:
 		splittedInstr = line.strip().split(" ")
 		instr.append(splittedInstr)

visited = [False] * len(instr)

i = 0
acc = 0

while not(visited[i]):
	visited[i] = True
	number = int(instr[i][1])
	if instr[i][0] == "acc":
		acc += number
		i += 1
	elif instr[i][0] == "jmp":
		i += number
	elif instr[i][0] == "nop":
		i += 1

print(acc)