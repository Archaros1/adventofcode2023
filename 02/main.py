file1 = open('input', 'r')
lines = file1.readlines()

# part 1
print("Part 1")
limits = {
  'red': 12,
  'green': 13,
  'blue': 14,
}
sumValidIds = 0
for line in lines:
  isValid = True
  game = line.replace("\n", '').split(': ')

  sets = game[1].split('; ')
  for set in sets:
    grabs = set.split(', ')

    for grab in grabs:
      grab = grab.split(' ')
      if int(grab[0]) > int(limits[grab[1]]):
        isValid = False
        break
      
    if not isValid:
      break

  if isValid:
    id = int(game[0].replace('Game ', ''))
    sumValidIds += id

print(sumValidIds)

# part 2
print("Part 2")
totalPower = 0
for line in lines:
  game = line.replace("\n", '').split(': ')

  minimalSet = {
    'blue': 0,
    'green': 0,
    'red': 0,
  }
  sets = game[1].split('; ')
  for set in sets:
    grabs = set.split(', ')

    for grab in grabs:
      grab = grab.split(' ')
      minimalSet[grab[1]] = max([int(grab[0]), minimalSet[grab[1]]])

  print(minimalSet)
  power = minimalSet['blue'] * minimalSet['green'] * minimalSet['red']
  totalPower += power

print(totalPower)
