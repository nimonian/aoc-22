solution = {'a': 0, 'b': 0}

with open('./08-input.txt', 'r') as f:
    F = [[int(x) for x in row.strip()] for row in f.readlines()]


def _max(L):
    return max(L) if len(L) else -1


def get_vistas(r, c, A):
    row = A[r]
    col = [_row[c] for _row in A]
    return [row[c+1:], row[:c][::-1], col[r+1:], col[:r][::-1]]


def count_visible(A):
    count = 0
    for r in range(len(A)):
        for c in range(len(A[r])):
            if A[r][c] > min(map(_max, get_vistas(r, c, A))):
                count += 1
    return count


def viewing_distance(x, L):
    d = 0
    for y in L:
        d += 1
        if y >= x:
            break
    return d


def max_scenic_score(A):
    res = 0
    for r in range(len(A)):
        for c in range(len(A[r])):
            score = 1
            for vista in get_vistas(r, c, A):
                score *= viewing_distance(A[r][c], vista)
            if score > res:
                res = score
    return res


solution['a'] = count_visible(F)
solution['b'] = max_scenic_score(F)

print(solution)
