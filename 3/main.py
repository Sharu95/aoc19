def travel(directions, to=False):
	seen, cur_x, cur_y, total_steps = [], 0, 0, 0
	x, y = to if to else (None, None)
	decode = { 'R': 1, 'L': -1, 'U': -1, 'D': 1 }

	for instruction in directions:
		steps, direction = int(instruction[1:]), instruction[0]
		for _ in range(1, steps + 1):
			has_arrived = cur_x == x and cur_y == y
			if direction in ['R', 'L']: 
				cur_x += decode[direction]
			else: 
				cur_y += decode[direction]
			
			total_steps += 1
			
			if to and has_arrived: 
				return total_steps
			else: 
				seen.append((cur_x, cur_y))
	return seen 

def main(w1, w2):
	# Part 1
	seen_w1 = set(travel(w1))
	seen_w2 = set(travel(w2))
	ixns = seen_w1.intersection(seen_w2)
	distances = map(lambda tpl: abs(tpl[0]) + abs(tpl[1]), ixns)
	print(min(distances))

	# Part 2
	time_delays = [ travel(w1, to=ixn) + travel(w2, to=ixn) for ixn in ixns ]
	print(min(time_delays))

if __name__ == '__main__':
	with open('input.txt', 'r') as f:
		w1, w2 = f.readlines()
		w1, w2 = w1.split(','), w2.split(',')
		main(w1, w2)