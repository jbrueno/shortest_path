from array import *
from copy import copy, deepcopy
from operator import attrgetter
from math import *

#profile the memory usage
#from guppy import hpy
#h = hpy()
#print h.heap()


depth = 20  # depth used for iterative deepening search
acts = []   # array of actions that lead to goal state found by iterative deepening
score = []

class Action:
	def __init__(self, direction, row, column, value):
		self.direction = direction
		self.row = row
		self.column = column
		self.value = value
	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)
	def __repr__(self):
		return str(self)

class Aboard:
	def __init__(self, board, h_score, parent):
		self.board = board
		self.h_score = h_score
		self.parent = parent
	def __str__(self):
		return str(self.__dict__)
	def __repr__(self):
		return str(self.board)

goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
board0 = [[3, 1, 2], [7, 0, 5], [4, 6, 8]]
board1 = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]
board2 = [[6, 7, 3], [1, 5, 2], [4, 0, 8]]
board3 = [[0, 8, 6], [4, 1, 3], [7, 2, 5]]
board4 = [[7, 3, 4], [2, 5, 1], [6, 8, 0]]
board5 = [[1, 3, 8], [4, 7, 5], [6, 0, 2]]
board6 = [[8, 7, 6], [5, 4, 3], [2, 1, 0]]
aboard0 = Aboard(board0, None, None)
aboard1 = Aboard(board1, None, None)
aboard2 = Aboard(board2, None, None)
aboard3 = Aboard(board3, None, None)
aboard4 = Aboard(board4, None, None)
aboard5 = Aboard(board5, None, None)
aboard6 = Aboard(board6, None, None)


# returns the list of all possible actions that can be performed on the given board
def possible_actions(board):
	possible = []
	for i in range(len(board)):
		for j in range(3):
			#check if you can move right
			if j != 2:
				if board[i][j] != 0:
					if board[i][j+1] == 0:
						a = Action("right", i, j, board[i][j])
						possible.append(a)
			#check if you can move left
			if j != 0:
				if board[i][j] != 0:
					if board[i][j-1] == 0:
						a = Action("left", i, j, board[i][j])
						possible.append(a)
			#check if you can move up
			if i != 0:
				if board[i][j] != 0:
					if board[i-1][j] == 0:
						a = Action("up", i, j, board[i][j])
						possible.append(a)
			#check if you can move down
			if i != 2:
				if board[i][j] != 0:
					if board[i+1][j] == 0:
						a = Action("down", i, j, board[i][j])
						possible.append(a)
	return possible


# returns a copy of the board after the specified action is applied to it
def result(Action, board):
	board_cpy = deepcopy(board)
	
	if Action.direction == "right":
		tmp = board_cpy.board[Action.row][Action.column]
		board_cpy.board[Action.row][Action.column] = board_cpy.board[Action.row][Action.column+1]
		board_cpy.board[Action.row][Action.column+1] = tmp
	if Action.direction == "left":
		tmp = board_cpy.board[Action.row][Action.column]
		board_cpy.board[Action.row][Action.column] = board_cpy.board[Action.row][Action.column-1]
		board_cpy.board[Action.row][Action.column-1] = tmp
	if Action.direction == "up":
		tmp = board_cpy.board[Action.row][Action.column]
		board_cpy.board[Action.row][Action.column] = board_cpy.board[Action.row-1][Action.column]
		board_cpy.board[Action.row-1][Action.column] = tmp
	if Action.direction == "down":
		tmp = board_cpy.board[Action.row][Action.column]
		board_cpy.board[Action.row][Action.column] = board_cpy.board[Action.row+1][Action.column]
		board_cpy.board[Action.row+1][Action.column] = tmp

	board_cpy.parent = board
	return board_cpy

# returns all possible outcomes of the board given the possible actions
def expand(board):
	possible = []
	actions = possible_actions(board.board)
	for act in actions:
		possible.append(result(act, board))
	return possible

# find the path cost to get to the given board by counting its parents
def path_cost(board):
	sum = 0
	board_cpy = deepcopy(board)
	while(board_cpy.parent != None):
		sum+=1
		board_cpy = board_cpy.parent
	board.h_score = sum
	return sum

# prints out list of all the boards parents
def print_parent(board):
	tmp = deepcopy(board)
	print(tmp.board)
	while tmp.parent != None:
		print(tmp.parent.board)
		tmp = tmp.parent


# add the nummber of misplaced tiles on the board
def misplaced(board):
	sum = 0
	if board.board[0][0] != 0:
		sum+=1
	if board.board[0][1] != 1:
		sum+=1
	if board.board[0][2] != 2:
		sum+=1
	if board.board[1][0] != 3:
		sum+=1
	if board.board[1][1] != 4:
		sum+=1
	if board.board[1][2] != 5:
		sum+=1
	if board.board[2][0] != 6:
		sum+=1
	if board.board[2][1] != 7:
		sum+=1
	if board.board[2][2] != 8:
		sum+=1
	return sum

# find the manhattan distance of the given board
def manhattan(board):
	targeti=0
	targetj=0
	dist = 0
	for i in range(3):
		for j in range(3):
			val = board.board[i][j]
			if val != 0:
				if val == 1:
					targeti = 0
					targetj = 1
					dist+= abs(i - targeti) + abs(j - targetj)
				if val == 2:
					targeti = 0
					targetj = 2
					dist+= abs(i - targeti) + abs(j - targetj)
				if val == 3:
					targeti = 1
					targetj = 0
					dist+= abs(i - targeti) + abs(j - targetj)
				if val == 4:
					targeti = 1
					targetj = 1
					dist+= abs(i - targeti) + abs(j - targetj)
				if val == 5:
					targeti = 1
					targetj = 2
					dist+= abs(i - targeti) + abs(j - targetj)
				if val == 6:
					targeti = 2
					targetj = 0
					dist+= abs(i - targeti) + abs(j - targetj)
				if val == 7:
					targeti = 2
					targetj = 1
					dist+= abs(i - targeti) + abs(j - targetj)
				if val == 8:
					targeti = 2
					targetj = 2
					dist+= abs(i - targeti) + abs(j - targetj)
	board.h_score = dist


# depth-first-search with a limit of 'depth' called by iterative_deepening
def lim_dfs(board, depth):
	possible = len(possible_actions(board.board))

	if(board.board == goal):
		print("success")
		print(board.board)
		return True

	if depth == 0:
		return False

	for poss in range(0, possible):
		if depth == 0:
			return False
		depth -= 1
		if lim_dfs(expand(board)[poss], depth): # recurse down the different states, but only 'depth' times
			return True

	return False

# performs an iterative deepening search on the board looking for 'goal'
def iterative_deepening(board):
	board_cpy = deepcopy(board)

	if(board_cpy.board == goal):
		return True

	for i in range(0, depth):
		if(lim_dfs(board_cpy, depth)):
			return True

	print("iterative deepening search failed")
	return False



# perform an A* search on the given board using h as the heuristic function
def astar_search(board, h):
	open_list = []
	closed = []

	open_list.append(board)

	if board == goal:
		return True

	board.h_score = h(board)

	while len(open_list) != 0:
		map(h, open_list) # apply heuristic to all boards on the open list

		current = min(open_list, key = attrgetter('h_score')) # select the lowest h_score to be the board we explore

		open_list.remove(current)
		closed.append(current.board)

		if current.board == goal:
			print("A* completed with final board: ")
			print(current.board)
			print("Number of moves: " + str(path_cost(current)))
			return True

		children = expand(current)

		for child in children:
			if child.board in closed:
				continue
			if child not in open_list:
				open_list.append(child)
			else:
	  			index = open_list.index(child)
	  			tmp = open_list[index]
	  			if child.h_score < tmp.h_score:
	  				tmp.parent = child.parent
	  				tmp.board = child.board
	  				tmp.h_score = child.h_score
	  				open_list.append(tmp)
	print("A* failed")
	return False


#astar_search(aboard2, manhattan)

#iterative_deepening(aboard0)
