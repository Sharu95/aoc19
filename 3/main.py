central_port = (8, 1)
w1 = "R8,U5,L5,D3"
w2 = "U7,R6,D4,L4"
import numpy as np 

right = lambda p, delta: (p[0] + delta, p[1])
left = lambda p, delta: (p[0] - delta, p[1])
down = lambda p, delta: (p[0], p[1] + delta)
up = lambda p, delta: (p[0], p[1] - delta)

def main(w1, w2):

	w1_path = {}
	current_point = central_port
	for direction in w1: 
		d = int(direction[1:])
		point = None
		if 'R' in direction:
			point = right(current_point, d)
		elif 'U' in direction:
			point = up(current_point, d)
		elif 'L' in direction:
			point = left(current_point, d)
		elif 'D' in direction:
			point = down(current_point, d)
		else:
			print('Unknown')
		
		w1_path[point] = True
	
	for direction in w2:
		d = int(direction[1:])
		point = None
		if 'R' in direction:
			point = right(current_point, d)
		elif 'U' in direction:
			point = up(current_point, d)
		elif 'L' in direction:
			point = left(current_point, d)
		elif 'D' in direction:
			point = down(current_point, d)
		else:
			print('Unknown')
		
		if point in w1_path:
			print('Crosses at', point) 

if __name__ == '__main__':
	with open('input.txt', 'r') as f:
		_ = f.read()

		w1, w2 = w1.split(','), w2.split(',')
		main(w1, w2)
