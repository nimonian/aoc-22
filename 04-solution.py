solution = { 'a': 0, 'b': 0 }

with open('./04-input.txt', 'r') as f:
  pairs = [pair.strip().split(',') for pair in f.readlines()]

for pair in pairs:
  pair = [[int(x) for x in area.split('-')] for area in pair]
  pair.sort()
  solution['a'] += pair[0][0] == pair[1][0] or pair[1][1] <= pair[0][1]
  solution['b'] += pair[0][1] >= pair[1][0]

print(solution)
