__author__ = 'shivani'
# This is the Backtracking Algorithm that finds the Knight's Tour (open) using recursion
# Python version: 3.4
# Execution: python backtracking.py
import time

grid = None


def main():
	# accepts size >= 5
	for i in range(5, 6):
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


def find_tour(size, x, y, move_index):
	global grid
	possible_moves = 8
	# x_moves = [2, 1, -1, -2, -2, -1,  1,  2]  # the 8 possible moves from any point
	# y_moves = [1, 2, 2,   1, -1, -2, -2, -1]

	moves = [(2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1, -2), (1, -2), (2, -1)]

	# base case:
	if move_index == size*size:
		# print("Max number of moves reached = %d" % move_index)
		return True

	for i in range(possible_moves):
		x_next = x + moves[i][0]
		y_next = y + moves[i][1]
		# print(grid)
		# print("move#: %d, (x,y)=(%d,%d)" % (move_index, x, y))
		if valid_move(x_next, y_next, size):
			next_move = move_index+1
			grid[x_next][y_next] = move_index

			if find_tour(size, x_next, y_next, next_move):
				return True
			else:  # Backtrack the previous moves
				grid[x_next][y_next] = -1

	return False


def valid_move(x, y, size):
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

main()