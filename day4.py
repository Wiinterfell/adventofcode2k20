import sys

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
 				if name in fields:
 					fields[name] = True

# check if valid
fieldCount = 0
for value in fields.values():
 	if value:
 		fieldCount += 1
 	if (fieldCount == 8 or (fieldCount == 7 and fields["cid"] == False)):
 		validCount += 1
			
print(validCount)