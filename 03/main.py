file1 = open('input copy', 'r')
lines = file1.readlines()

# part 1
print("Part 1")
numbers = []
for lineKey, line in enumerate(lines):
  line = line.replace("\n", '')
  inNumber = False
  for charKey, char in enumerate(line):
    if char.isnumeric():
      if not inNumber:
        inNumber = True
        newNumber = {
          "lineKey": lineKey,
          "charKey": charKey,
          "length": 1,
          "value": char
        }
      else:
        newNumber['length'] += 1
        newNumber['value'] += char
    else:
      if inNumber:
        numbers.append(newNumber)
        print(newNumber)
        inNumber = False

# print(numbers)