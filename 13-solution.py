from functools import cmp_to_key

solution = {'a': 0, 'b': 0}

with open('./13-input.txt', 'r') as f:
    lines = f.read().strip()
    singles = lines.replace('\n\n', '\n').split('\n')
    singles = [eval(single.strip()) for single in singles]
    pairs = lines.strip().split('\n\n')
    pairs = [pair.split('\n') for pair in pairs]
    pairs = [list(map(eval, packet)) for packet in pairs]


def make_list(x):
    return x if isinstance(x, list) else [x]


def right_order(p1, p2):
    for x, y in zip(p1, p2):

        if isinstance(x, int) and isinstance(y, int):
            if x == y:
                continue
            return x < y

        res = right_order(make_list(x), make_list(y))

        if res == None:
            continue

        return res

    if len(p1) == len(p2):
        return

    return len(p1) < len(p2)

def cmp(p1, p2):
    return 1 if right_order(p1, p2) else -1

solution['a'] = sum([i + 1 for i, p in enumerate(pairs)
                    if right_order(p[0], p[1])])

singles.append([[2]])
singles.append([[6]])

singles = sorted(singles, key=cmp_to_key(cmp), reverse=True)

solution['b'] = (singles.index([[2]]) + 1) * (singles.index([[6]]) + 1)

print(solution)