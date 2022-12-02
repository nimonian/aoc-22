with open('01-input.txt', 'r') as f:
  elves = f.read().strip().split('\n\n')

elves = [elf.strip().split('\n') for elf in elves]
elves = [sum([int(x) for x in elf]) for elf in elves]

# part a
print(max(elves))

# part b
elves.sort()
print(sum(elves[-3:]))
