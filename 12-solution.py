import math

solution = {'a': 0, 'b': 0}

with open('./12-input.txt', 'r') as f:
    M = []
    for (r, row) in enumerate([l.strip() for l in f.readlines()]):
        M.append([])
        for (c, char) in enumerate(row):
            node = {
                'char': char,
                'height': ord(char) - 96,
                'distance': math.inf,
                'visited': False,
                'position': (r, c)
            }
            if char == 'S':
                node['char'] = 'a'
                node['height'] = ord('a') - 96
                node['distance'] = 0
            if char == 'E':
                node['char'] = 'z'
                node['height'] = ord('z') - 96
                E = node
            M[-1].append(node)


def v_add(u, v):
    return tuple(x + y for x, y in zip(u, v))


def get_node(p):
    return M[p[0]][p[1]]


def get_neighbours(n):
    U = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    N = [v_add(n['position'], u) for u in U]
    N = [m for m in N if (0 <= m[0] < len(M)) and (0 <= m[1] < len(M[m[0]]))]
    N = [get_node(m) for m in N]
    N = [m for m in N if m['height'] <= n['height'] + 1]
    N = [m for m in N if not m['visited']]
    return N


def dijkstra():
    nodes = [P for r in M for P in r]
    while E['visited'] == False:
        nodes.sort(key=lambda n: n['distance'])
        n = nodes.pop(0)
        n['visited'] = True
        for m in get_neighbours(n):
            m['distance'] = min(m['distance'], n['distance'] + 1)
    return n['distance']


print(dijkstra())
