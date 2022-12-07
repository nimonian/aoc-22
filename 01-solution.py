solution = {'a': 0, 'b': 0}

with open('01-input.txt', 'r') as f:
    elves = f.read().strip().split('\n\n')

elves = [elf.strip().split('\n') for elf in elves]
elves = [sum([int(x) for x in elf]) for elf in elves]

elves.sort()
solution['a'] = elves[-1]
solution['b'] = sum(elves[-3:])

print(solution)
