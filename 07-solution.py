solution = {'a': 0, 'b': 0}

with open('./07-input.txt', 'r') as f:
	stdout = [line.strip() for line in f.readlines()]


def get_path_meta(lines):
	loc = ['~']
	d = {}
	for line in lines[1:]:
		if line == '$ cd ..': loc = loc[:-1]
		elif line[:4] == '$ cd': loc.append(line[5:])
		else:
			s = line.split(' ')[0]
			if s.isdigit():
				for i in range(len(loc)):
					path = '/'.join(loc[:i+1])
					d[path] = int(s) + d.get(path, 0)
	return d


meta = get_path_meta(stdout)

solution['a'] = sum(meta[p] for p in meta if meta[p] <= 10**5)

free_space = 7*10**7 - meta['~']
to_delete = 3*10**7 - free_space

solution['b'] = min(meta[p] for p in meta if meta[p] >= to_delete)

print(solution)
