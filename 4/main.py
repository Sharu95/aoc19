is_increasing = lambda pwd: not True in [pwd[i] > pwd[i + 1] for i in range(len(pwd) - 1)]

# If we know that each succeeding value is greater,
# then multiple occurrences of the same number must be 
# adjacent (not 6 unique elements)
has_adjacent = lambda pwd: len(set(pwd)) != 6

def is_larger_group(pwd):
	groups = dict([(char, pwd.count(char)) for char in pwd])
	return not 2 in groups.values()

def is_valid(pwd, part_2=False):
	s = str(pwd)
	criteria = (part_2 and is_larger_group(s)) or (not has_adjacent(s) or not is_increasing(s))
	return False if criteria else s	

if __name__ == '__main__':
	with open('input.txt', 'r') as f:
		FROM, TO = map(int, f.read().split(','))

		# Part 1
		a = [is_valid(p) for p in range(FROM, TO + 1)]
		a = list(filter(lambda x: x, a))
		print(len(a))

		# Part 2
		v = [is_valid(p, part_2=True) for p in a]
		v = list(filter(lambda x: x, v))
		print(len(v))