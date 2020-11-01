# shortest_path
AI shortest path algorithms

Implemented an A* search and iterative deepening search to solve the n-puzzle problem.  
The boards used are 3x3 with numbers ranging from 1-8.  The 0 is used to represent the
empty square which allows the 'tiles' to be shifted on the board.  
The A* search is most efficient when run with the Manhattan Distance as its heuristic.  In all 
cases, iterative deepening performs much slower than the A* search because of the need to expand
many more board states.  This illustrates how beneficial it is to use an informed search algorithm
even if its heuristic function is as simple as the manhattan distance.
For testing purposes, the goal state is always the numbers in order with the top left of the board
(index[0][0]) being 0 or empty.
