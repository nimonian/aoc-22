solution = {'a': 0, 'b': 0}

rock = set()
sand = set()

with open('./14-input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    
    for line in lines:
        points = [eval(f'({point})') for point in line.split(' -> ')]
        for p, q in zip(points[:-1], points[1:]):
            if p[0] == q[0]:
                rock |= {(p[0], y)
                         for y in range(min(p[1], q[1]), max(p[1], q[1]) + 1)}
            if p[1] == q[1]:
                rock |= {(x, p[1]) for x in range(
                    min(p[0], q[0]), max(p[0], q[0]) + 1)}

bottom = max(p[1] for p in rock)

def v_add(u, v):
    return tuple(x + y for x, y in zip(u, v))


def drop_sand():
    global rock, sand, bottom
    p = (500, 0)
    d, l, r = (0, 1), (-1, 1), (1, 1)

    while True:
        if not v_add(p, d) in rock | sand:
            p = v_add(p, d)
            if p[1] == bottom:
                return
            continue
        if not v_add(p, l) in rock | sand:
            p = v_add(p, l)
            if p[1] == bottom:
                return
            continue
        if not v_add(p, r) in rock | sand:
            p = v_add(p, r)
            if p[1] == bottom:
                return
            continue
        sand.add(p)
        break

    drop_sand()

drop_sand()
print(len(sand))
