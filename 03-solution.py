solution = {"a": 0, "b": 0}


def getBags(path):
    with open(path, "r") as f:
        bags = [l.strip() for l in f.readlines()]
    return bags


def priority(c):
    return ord(c) - (96 if c == c.lower() else 38)


bags = getBags("./03-input.txt")
for bag in bags:
    n = len(bag) // 2
    c = (set(bag[:n]) & set(bag[n:])).pop()
    solution["a"] += priority(c)

bags = getBags("./03-input.txt")
for i in range(len(bags) // 3):
    b1, b2, b3 = bags[3 * i : 3 * (i + 1)]
    c = (set(b1) & set(b2) & set(b3)).pop()
    solution["b"] += priority(c)

print(solution)
