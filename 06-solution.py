solution = {'a': 0, 'b': 0}

with open('./06-input.txt', 'r') as f:
	stream = f.read()


def get_start(stream, n):
	for i in range(len(stream) - n):
		if len(set(stream[i:i+n])) == n: return i + n


solution['a'] = get_start(stream, 4)
solution['b'] = get_start(stream, 14)

print(solution)
