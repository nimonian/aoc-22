from time import time

taken = set()

with open('./14-input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

    for line in lines:
        points = [eval(f'({point})') for point in line.split(' -> ')]
        for p, q in zip(points[:-1], points[1:]):
            if p[0] == q[0]:
                taken |= {(p[0], y)
                         for y in range(min(p[1], q[1]), max(p[1], q[1]) + 1)}
            if p[1] == q[1]:
                taken |= {(x, p[1]) for x in range(
                    min(p[0], q[0]), max(p[0], q[0]) + 1)}

rock_count = len(taken)
bottom = max(p[1] for p in taken) + 2


def v_add(u, v):
    return tuple(x + y for x, y in zip(u, v))

t0 = time()
full = False
while not full:
    p = (500, 0)
    d, l, r = (0, 1), (-1, 1), (1, 1)

    if {v_add(p, d), v_add(p, l), v_add(p, r)}.issubset(taken):
        taken.add(p)
        full = True

    while True:
        if v_add(p, d)[1] == bottom:
            taken.add(p)
            break
        if not v_add(p, d) in taken:
            p = v_add(p, d)
            continue
        if not v_add(p, l) in taken:
            p = v_add(p, l)
            continue
        if not v_add(p, r) in taken:
            p = v_add(p, r)
            continue
        taken.add(p)
        break

print(len(taken) - rock_count)
