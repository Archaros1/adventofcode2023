import re

file1 = open('input', 'r')
Lines = file1.readlines()

numbers = [
  'zero',
  'one',
  'two',
  'three',
  'four',
  'five',
  'six',
  'seven',
  'eight',
  'nine',
]

# Part 1
sum = 0
for line in Lines:
  finds = []
  pattern = '([0-9])'
  output = re.search(pattern, line)
  finds.append(output[0])
  output = re.search(pattern, line[::-1])
  finds.append(output[0])
  sum += (int(finds[0]) * 10) + int(finds[1])

print(sum)

# Part 2
sum = 0
for line in Lines:
  finds = []
  pattern = '([0-9]|' + '|'.join(numbers) + ')'
  output = re.findall(pattern, line)
  finds.append(output[0])
  pattern = '^.*([0-9]|' + '|'.join(numbers) + ')'
  output = re.findall(pattern, line)
  finds.append(output[0])

  if len(finds[0]) > 1:
    finds[0] = numbers.index(finds[0])
  else:
    finds[0] = int(finds[0])

  if len(finds[1]) > 1:
    finds[1] = numbers.index(finds[1])
  else:
    finds[1] = int(finds[1])
  
  sum += (finds[0] * 10) + finds[1]

print(sum)