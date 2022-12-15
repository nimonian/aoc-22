import math

solution = {'a': 0, 'b': 0}

with open('./12-input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

M = []
for (r, row) in enumerate(lines):
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
            node['height'] = ord('a') - 96
        if char == 'E':
            node['height'] = ord('z') - 96
            E = node
        M[-1].append(node)


# add two tuples vector style, e.g. (1, 2) + (3, 4) = (4, 6)
def v_add(u, v):
    return tuple(x + y for x, y in zip(u, v))

# get the node at a given position in the map
def get_node(p):
    return M[p[0]][p[1]]

# flat map the map :/
def get_nodes(M):
    return [node for row in M for node in row]

# get a list of all unvisited neighbours represented as nodes
def get_neighbours(n):
    U = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    N = [v_add(n['position'], u) for u in U]
    N = [m for m in N if (0 <= m[0] < len(M)) and (0 <= m[1] < len(M[m[0]]))]
    N = [get_node(m) for m in N]
    N = [m for m in N if m['height'] >= n['height'] - 1]
    N = [m for m in N if not m['visited']]
    return N

# do the hustle! https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
def dijkstra():
    nodes = get_nodes(M)
    E['distance'] = 0
    while len(nodes):
        nodes.sort(key=lambda n: n['distance'])
        n = nodes.pop(0)
        n['visited'] = True
        for m in get_neighbours(n):
            m['distance'] = min(m['distance'], n['distance'] + 1)

dijkstra()

nodes = get_nodes(M)
solution['a'] = min([n['distance'] for n in nodes if n['char'] in ['S']])
solution['b'] = min([n['distance'] for n in nodes if n['char'] in ['a', 'S']])

print(solution)
