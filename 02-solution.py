solution = {"a": 0, "b": 0}

with open("02-input.txt", "r") as f:
    games = ["".join(game.split()) for game in f.readlines()]


def score_a(game):
    p1, p2 = "ABC".index(game[0]), "XYZ".index(game[1]) + 1
    result = (p2 - p1) % 3
    return p2 + result * 3


def score_b(game):
    p1, result = "ABC".index(game[0]), "XYZ".index(game[1])
    p2 = (p1 + result - 1) % 3 + 1
    return p2 + result * 3


solution["a"] = sum([score_a(game) for game in games])
solution["b"] = sum([score_b(game) for game in games])

print(solution)
