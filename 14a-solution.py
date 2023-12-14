import sys

sys.setrecursionlimit(1500)

solution = {"a": 0, "b": 0}

rock = set()
sand = set()

# get the coordinates of all pieces of rock
with open("./14-input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

    for line in lines:
        points = [eval(f"({point})") for point in line.split(" -> ")]
        for p, q in zip(points[:-1], points[1:]):
            if p[0] == q[0]:
                rock |= {
                    (p[0], y)  # "A |= B" means "A = A union B"
                    for y in range(min(p[1], q[1]), max(p[1], q[1]) + 1)
                }
            if p[1] == q[1]:
                rock |= {(x, p[1]) for x in range(min(p[0], q[0]), max(p[0], q[0]) + 1)}

bottom = max(p[1] for p in rock)

# add tuples vector style, e.g. (1, 2) + (3, 4) = (4, 6)


def v_add(u, v):
    return tuple(x + y for x, y in zip(u, v))


def drop_sand():
    global rock, sand, bottom
    p = (500, 0)
    # movement directions
    d, l, r = (0, 1), (-1, 1), (1, 1)

    while True:
        # if we can move down, do it!
        if not v_add(p, d) in rock | sand:  # | means union
            p = v_add(p, d)
            # but if we drop below the bottom, stop the simulation:
            if p[1] == bottom:
                return
            # otherwise loop to try and move again:
            continue
        # otherwise, try down-left:
        if not v_add(p, l) in rock | sand:
            p = v_add(p, l)
            if p[1] == bottom:
                return
            continue
        # ... and down-right:
        if not v_add(p, r) in rock | sand:
            p = v_add(p, r)
            if p[1] == bottom:
                return
            continue
        # if none of the above happens, it means we can't move
        # so get out of the loop...
        sand.add(p)
        break

    # ...and drop a new sand
    drop_sand()


drop_sand()
print(len(sand))
