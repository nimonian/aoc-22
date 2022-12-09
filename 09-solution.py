solution = {'a': 0, 'b': 0}

with open('./09-input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

step = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}


def v_mul(k, v):
    return tuple(k*x for x in v)


def v_add(u, v):
    return tuple(x + y for x, y in zip(u, v))


def v_unitize(v):
    return tuple(x // abs(x) if x else x for x in v)


def simulate(length):
    P = [[(0, 0)] for _ in range(length)]
    for line in lines:
        dir, k = line.split(' ')
        for _ in range(int(k)):
            P[0].append(v_add(P[0][-1], step[dir]))
            for h, t in zip(range(length - 1), range(1, length)):
                dx, dy = v_add(P[h][-1], v_mul(-1, P[t][-1]))
                if abs(dx) > 1 or abs(dy) > 1:
                    P[t].append(v_add(P[t][-1], v_unitize((dx, dy))))
    return len(set(P[length - 1]))


solution['a'] = simulate(2)
solution['b'] = simulate(10)

print(solution)
