import re

file1 = open('input', 'r')
lines = file1.readlines()

# part 1
print("Part 1")

total = 0
for lineKey, line in enumerate(lines):
  line = line.replace("\n", '')
  cardNumber = lineKey + 1
  cardWorth = 0
  numbers = line.split(': ')[1]
  numbers = numbers.split(' | ')
  winningNumbers = numbers[0]
  myNumbers = numbers[1]
  winningNumbers = re.findall('([0-9]{1,2})', winningNumbers)
  myNumbers = re.findall('([0-9]{1,2})', myNumbers)

  for number in myNumbers:
    if number in winningNumbers:
      if cardWorth == 0:
        cardWorth = 1
      else:
        cardWorth *= 2
  
  total += cardWorth

print(total)
