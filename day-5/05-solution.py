from copy import deepcopy

solution = {'a': '', 'b': ''}

with open('./05-input.txt', 'r') as f:
    txt = f.read().strip()

crates, dirs = txt.split('\n\n')
# wrangle crates
rows = crates.split('\n')[-2::-1]
stacks = [[row[4*i+1] for row in rows if row[4*i+1] != ' '] for i in range(9)]
# wrangle instructions
dirs = [[int(x) for x in dir.split(' ')[1::2]] for dir in dirs.split('\n')]
dirs = [{'move': dir[0], 'from': dir[1] - 1, 'to': dir[2] - 1} for dir in dirs]


def crane9000(stacks, dirs):
    stacks = deepcopy(stacks)
    for dir in dirs:
        stacks[dir['to']] += stacks[dir['from']][-1:-dir['move']-1:-1]
        stacks[dir['from']] = stacks[dir['from']][:-dir['move']]
    return ''.join([stack[-1] for stack in stacks])


def crane9001(stacks, dirs):
    stacks = deepcopy(stacks)
    for dir in dirs:
        stacks[dir['to']] += stacks[dir['from']][-dir['move']:]
        stacks[dir['from']] = stacks[dir['from']][:-dir['move']]
    return ''.join([stack[-1] for stack in stacks])


solution['a'] = crane9000(stacks, dirs)
solution['b'] = crane9001(stacks, dirs)

print(solution)
