import sys
import string

def validate(name, value):
	if name == "byr":
		return (len(value) == 4 and value.isdigit())
	elif name == "iyr":
		return (value.isdigit() and int(value) >= 2010 and int(value) <= 2020)
	elif name == "eyr":
		return (value.isdigit() and int(value) >= 2020 and int(value) <= 2030)
	elif name == "hgt":
		if (value[-2:] == "cm"):
			height = value[:-2]
			return (height.isdigit() and int(height) >= 150 and int(height) <= 193)
		elif (value[-2:] == "in"):
			height = value[:-2]
			return (height.isdigit() and int(height) >= 59 and int(height) <= 76)
		else:
			return False
	elif name == "hcl":
		return (value[0] == "#" and len(value) == 7 and (value[1:].isdigit() or all(c in string.hexdigits for c in value[1:])))
	elif name == "ecl":
		return (value in ["amb", "blu", "brn", "gry ", "grn", "hzl", "oth"])
	elif name == "pid":
		return (len(value) == 9 and value.isdigit())
	elif name == "cid":
		return True
	else:
		return False


validCount = 0

fields = {}
fields["byr"] = False
fields["iyr"] = False
fields["eyr"] = False
fields["hgt"] = False
fields["hcl"] = False
fields["ecl"] = False
fields["pid"] = False
fields["cid"] = False

with open("day4.txt") as fp:
 	for line in fp:
 		if (line.strip() == ""):

 			# check if valid
 			fieldCount = 0
 			for value in fields.values():
 				if value:
 					fieldCount += 1
 			if (fieldCount == 8 or (fieldCount == 7 and fields["cid"] == False)):
 				validCount += 1

 			#restore
			fields["byr"] = False
			fields["iyr"] = False
			fields["eyr"] = False
			fields["hgt"] = False
			fields["hcl"] = False
			fields["ecl"] = False
			fields["pid"] = False
			fields["cid"] = False

 		else:
 			fieldArray = line.strip().split(" ")
 			for field in fieldArray:
 				name = field.split(":")[0]
 				val = field.split(":")[1].strip()
 				if validate(name, val):
 					fields[name] = True

# check if valid
fieldCount = 0
for value in fields.values():
 	if value:
 		fieldCount += 1
 	if (fieldCount == 8 or (fieldCount == 7 and fields["cid"] == False)):
 		validCount += 1
			
print(validCount)