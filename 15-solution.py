import re

solution = {'a': 0, 'b': 0}

with open('./15-input.txt', 'r') as f:
    lines = f.readlines()

D = {}


def not_beacon(row, l, r):
    if not row in D:
        D[row] = []
    D[row].append([l, r])


def merge_intervals(intervals):
    intervals.sort(key=lambda i: i[0])
    merged = [intervals[0]]
    for i in intervals[1:]:
        if i[0] > merged[-1][1]:
            merged.append(i)
        else:
            merged[-1][1] = max(merged[-1][1], i[1])
    return merged


def total_width(intervals):
    merged = merge_intervals(intervals)
    return sum(i[1] - i[0] for i in merged)


for (i, line) in enumerate(lines):
    a, b, x, y = [int(d) for d in re.findall('-?\d+', line)]
    radius = abs(x - a) + abs(y - b)
    for k in range(0, radius + 1):
        l, r = a - radius + k, a + radius - k
        for row in set([b - k, b + k]):
            not_beacon(row, l, r)
    print(f'Finished drawing diamond {i+1} of {len(lines)}')

solution['a'] = total_width(D[2*10**6])

for y in D:
    if not 0 <= y <= 4*10**6:
        continue
    merged = merge_intervals(D[y])
    if len(merged) > 1:
        x = merged[0][1] + 1
        if not 0 <= x <= 4*10**6:
            continue
        break

solution['b'] = 4*10**6 * x + y

print(solution)