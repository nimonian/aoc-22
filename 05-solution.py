solution = {'a': '', 'b': ''}

def getInput(path):
    with open(path, 'r') as f:
        txt = f.read().strip()
        crates, dirs = txt.split('\n\n')
    # wrangle crates
    rows = crates.split('\n')[-2::-1]
    stacks = [[row[4*i+1] for row in rows if row[4*i+1] != ' ']
              for i in range(9)]
    # wrangle instructions
    dirs = [[int(x) for x in dir.split(' ')[1::2]] for dir in dirs.split('\n')]
    dirs = [{'move': dir[0], 'from': dir[1] - 1, 'to': dir[2] - 1}
            for dir in dirs]
    return [stacks, dirs]


def crane9000():
    stacks, dirs = getInput('./05-input.txt')
    for dir in dirs:
        stacks[dir['to']] += stacks[dir['from']][-1:-dir['move']-1:-1]
        stacks[dir['from']] = stacks[dir['from']][:-dir['move']]
    return stacks


def crane9001():
    stacks, dirs = getInput('./05-input.txt')
    for dir in dirs:
        stacks[dir['to']] += stacks[dir['from']][-dir['move']:]
        stacks[dir['from']] = stacks[dir['from']][:-dir['move']]
    return stacks


solution['a'] = ''.join([stack[-1] for stack in crane9000()])
solution['b'] = ''.join([stack[-1] for stack in crane9001()])

print(solution)
