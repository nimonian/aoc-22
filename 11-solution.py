from copy import deepcopy

solution = {'a': 0, 'b': 0}

def modular_dict(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    return {p: n % p for p in primes}

with open('11-input.txt', 'r') as f:
    texts = f.read().strip().split('\n\n')
    M = []
    for text in texts:
        lines = text.split('\n')
        M.append({
            'items': [int(item) for item in lines[1].split(':')[1].split(',')],
            'op': f'{lines[2].split(" = ")[1]}',
            'prime': int(lines[3].split(" by ")[1]),
            'True': int(lines[4][-1]),
            'False': int(lines[5][-1]),
            'count': 0
        })

def a():
    _M = deepcopy(M)
    for _ in range(20):
        for m in _M:
            items = list(map(lambda old: eval(m['op']) // 3, m['items']))
            m['count'] += len(items)
            m['items'] = []
            for item in items:
                to = _M[m[str(item % m['prime'] == 0)]]
                to['items'].append(item)
    counts = [m['count'] for m in _M]
    counts.sort()
    return counts[-1] * counts[-2]

def b():
    _M = deepcopy(M)
    for m in _M:
        m['items'] = [modular_dict(item) for item in m['items']]
    for _ in range(10000):
        for m in _M:
            items = m['items']
            m['count'] += len(items)
            m['items'] = []
            f = lambda old: eval(m['op'])
            items = [{key: f(val) % key for key, val in item.items()} for item in items]
            for item in items:
                to = _M[m[str(item[m['prime']] == 0)]]
                to['items'].append(item)
    counts = [m['count'] for m in _M]
    counts.sort()
    return counts[-1] * counts[-2]

solution['a'] = a()
solution['b'] = b()

print(solution)
