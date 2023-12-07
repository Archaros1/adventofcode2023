import re

file1 = open('input', 'r')
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
      if charKey == len(line) - 1:
        newNumber['value'] = int(newNumber['value'])
        numbers.append(newNumber)
        inNumber = False
        print(newNumber)
    else:
      if inNumber:
        newNumber['value'] = int(newNumber['value'])
        numbers.append(newNumber)
        inNumber = False
        print(newNumber)

# print(numbers)

validNumbers = []
for number in numbers:
  minRangeLine = number['lineKey'] - 1 if number['lineKey'] - 1 >= 0 else 0
  maxRangeLine = number['lineKey'] + 1 if number['lineKey'] + 1 <= len(lines) - 1 else len(lines) - 1
  isValid = False
  for lineKey in range(minRangeLine, maxRangeLine + 1):
    minRangeChar = number['charKey'] - 1 if number['charKey'] - 1 >= 0 else 0
    maxRangeChar = number['charKey'] + number['length'] + 1 if number['charKey'] + number['length'] + 1 <= len(line) - 1 else len(line)
    
    for charKey in range(minRangeChar, maxRangeChar):
      if re.match('[^0-9\.]', lines[lineKey][charKey]):
        # character special
        validNumbers.append(number['value'])
        isValid = True
        print(number['value'], lines[lineKey][charKey])
        break
    if isValid:
      break

# print(validNumbers)
print(sum(validNumbers))