__author__ = 'shivani'
# This is the Backtracking Algorithm that finds the Knight's Tour (open) using recursion
# Python version: 3.4
# Execution: python backtracking.py
import time

grid = None


def __main__():
	# accepts size >= 5
	for i in range(5, 30):
		board_size = i
		knights_tour(board_size)


def knights_tour(size):
	global grid
	grid = [[-1 for i in range(size)] for i in range(size)]  # grid initialized to -1

	# starting position (0,0)
	x = y = 0
	grid[x][y] = 0

	start = time.time()
	found = find_tour(size, x, y, 1)
	end = time.time()
	print_tour(found, grid, size)
	print("(took %f seconds)" % (end - start))

def get_valid_moves(moves, x, y, size):
	return [move for move in moves if is_valid_move(x + move[0], y + move[1], size)]

def get_valid_moves_warnsdorff(moves, x, y, size):
	valid_moves = [(valid_move, len(get_valid_moves(moves, x + valid_move[0], y + valid_move[1], size))) for valid_move in get_valid_moves(moves, x, y, size)]
	sorted_moves = sorted(valid_moves, key=lambda w: w[1], reverse=False)
	return [move[0] for move in sorted_moves]

def find_tour(size, x, y, move_index):
	global grid
	possible_moves = 8
	moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

	# base case:
	if move_index == size*size:
		# print("Max number of moves reached = %d" % move_index)
		return True

	# [ move1, move2, ...]
	# valid_moves = get_valid_moves(moves, x, y, size)
	valid_moves = get_valid_moves_warnsdorff(moves, x, y, size)

	for valid_move in valid_moves:
		x_next = x + valid_move[0]
		y_next = y + valid_move[1]
		# print(grid)
		# print("move#: %d, (x,y)=(%d,%d)" % (move_index, x, y))
		next_move = move_index+1
		grid[x_next][y_next] = move_index

		if find_tour(size, x_next, y_next, next_move):
			return True
		else:  # Backtrack the previous moves
			grid[x_next][y_next] = -1

	return False

def is_valid_move(x, y, size):
	global grid
	valid = False
	if 0 <= x < size and 0 <= y < size and grid[x][y] == -1:  # if move not visited and inside boundary
		valid = True
	return valid


def print_tour(tour_found, board, size):
	print("\nKnight's Tour (%dx%d):" % (size, size))
	if tour_found:
		for x in board:
			print('\t'.join(map(str, x)))
	else:
		print("None found.")

__main__()
