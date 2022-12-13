solution = {'a': 0, 'b': ''}

with open('./10-input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

cycle, x = 1, 1
sample = [20 + i * 40 for i in range(6)]


def tick(y):
    global cycle, x
    if cycle in sample: solution['a'] += cycle * x
    solution['b'] += '#' if (cycle - 1) % 40 in [x - 1, x, x + 1] else '.'
    x += y
    cycle += 1


for line in lines:
    op = line[:4]
    if op == 'noop':
        tick(0)
    if op == 'addx':
        y = int(line.split(' ')[1])
        tick(0)
        tick(y)


print(solution['a'])
for row in [solution['b'][40*i:40*(i + 1)] for i in range(6)]:
    print(row)
