#import for random side selection
import random
import math
from collections import OrderedDict
import pygame

#maze and path are the global variable for the whole program
maze = []
path = []

#Class to declare structure of each cell of maze
class Cell():
	def __init__(self):
		self.visit = False
		self.top = True
		self.down = True
		self.left = True
		self.right = True


	#Build a 2D array or list with height and width
	def initializeMaze():
		global maze
		maze = [[Cell() for row in range(height)] for col in range(width)]


	#This fucntion is recursive calling to every neighbouring node and backtracking once it is DFSed.
	def routeNeighbour(row,col):
		global maze
		maze[row][col].visit = True

		#Create an array or list of possible side to break down the wall
		ran_case = ["left","right","top","down"]
		random.shuffle(ran_case)
		for ran in ran_case:
			if ran == "left":
				if Cell.pointValid(row,col-1) and maze[row][col-1].visit == False:
					maze[row][col].left = False
					maze[row][col-1].right = False
					Cell.displayMaze(row, col-1)
					Cell.routeNeighbour(row,col-1)

			if ran == "right":
				if Cell.pointValid(row,col+1) and maze[row][col+1].visit == False:
					maze[row][col].right = False
					maze[row][col+1].left = False
					Cell.displayMaze(row,col+1)
					Cell.routeNeighbour(row,col+1)

			if ran == "top":
				if Cell.pointValid(row-1,col) and maze[row-1][col].visit == False:
					maze[row][col].top = False
					maze[row-1][col].down = False
					Cell.displayMaze(row-1,col)
					Cell.routeNeighbour(row-1,col)

			if ran == "down":
				if Cell.pointValid(row+1,col) and maze[row+1][col].visit == False:
					maze[row][col].down = False
					maze[row+1][col].top = False
					Cell.displayMaze(row+1,col)
					Cell.routeNeighbour(row+1,col)

				
	#This is a function that validates whether the next cell is valid or not
	def pointValid(row,col):
		if row>=0 and row<= width-1 and col>=0 and col<= height-1:
			return True
		return False


	#This function checks whether all cells are visited before exiting the code
	def allVisited():
		for row in range(width):
			for col in range(height):
				if maze[row][col].visit == False:
					return False
		return True

		
	#This function displays the maze in the pygame window
	def displayMaze(row, col):
		x_pos = col*size
		y_pos = row*size
		pygame.draw.rect(maze_display,(255,255,255),(x_pos,y_pos,size,size))

		if (maze[row][col].top):
			pygame.draw.line(maze_display, (0,0,0), (x_pos, y_pos), (x_pos+size, y_pos), size//10)
		else:
			pygame.draw.line(maze_display, (255,255,255), (x_pos, y_pos), (x_pos+size, y_pos), size//10)
		# pygame.display.update()
		# pygame.time.delay(30)

		if (maze[row][col].right):
			pygame.draw.line(maze_display, (0,0,0), (x_pos+size, y_pos), (x_pos+size, y_pos+size), size//10)
		else:
			pygame.draw.line(maze_display, (255,255,255), (x_pos+size, y_pos), (x_pos+size, y_pos+size), size//10)
		# pygame.display.update()
		# pygame.time.delay(30)

		if (maze[row][col].down):
			pygame.draw.line(maze_display, (0,0,0), (x_pos, y_pos+size), (x_pos+size, y_pos+size), size//10)
		else:
			pygame.draw.line(maze_display, (255,255,255), (x_pos, y_pos+size), (x_pos+size, y_pos+size), size//10)
		# pygame.display.update()
		# pygame.time.delay(30)

		if (maze[row][col].left):
			pygame.draw.line(maze_display, (0,0,0), (x_pos, y_pos), (x_pos, y_pos+size), size//10)
		else:
			pygame.draw.line(maze_display, (255,255,255), (x_pos, y_pos), (x_pos, y_pos+size), size//10)
		# pygame.display.update()
		# pygame.time.delay(30)



class Distance():
	def __init__(self):
		self.f_dist = 0
		self.h_dist = 0
		self.g_dist = 0
		self.chose = False
		self.visit = False
		self.select = False

	#Build a 2D array or list with distances to save
	def initializeDist():
		global path
		path = [[Distance() for row in range(height)] for col in range(width)]

	#This function finds the distances between all the possible cells
	def distCalculation():
		global path
		index_list = [[0,1],[0,-1],[1,0],[-1,0]]
		side_list = ["right", "left", "down", "top"]
		stack_od = OrderedDict()
		row, col = mazeStart_X, mazeStart_Y
		stack_od[row, col] = 0
		
		stack_index = 0
		while stack_od:
			[row, col], fa_value = list(stack_od.items())[stack_index]
			pygame.draw.rect(maze_display,(158,175,225),((col*size)+(size//2),(row*size)+(size//2),(size//10),(size//10)))
			# pygame.display.update()
			# pygame.time.delay(30)
			stack_od.popitem(last=False)
			path[row][col].chose = True
			if row == mazeEnd_X and col == mazeEnd_Y:
				break
			
			for index in range(len(index_list)):
				row_index, col_index = index_list[index]
				side = side_list[index]
				barrier = False
				if side == "right":
					barrier = maze[row][col].right
				elif side == "left":
					barrier = maze[row][col].left
				elif side == "top":
					barrier = maze[row][col].top
				elif side == "down":
					barrier = maze[row][col].down
				if Cell.pointValid(row+row_index, col+col_index) and not barrier and not path[row+row_index][col+col_index].chose:
					path[row+row_index][col+col_index].g_dist = int(10 * math.dist([mazeStart_X, mazeStart_Y], [row+row_index, col+col_index]))
					path[row+row_index][col+col_index].h_dist = int(10 * math.dist([mazeEnd_X, mazeEnd_Y], [row+row_index, col+col_index]))
					path[row+row_index][col+col_index].f_dist = path[row+row_index][col+col_index].h_dist + path[row+row_index][col+col_index].g_dist
					if [row+row_index, col+col_index] in list(stack_od.keys()):
						stack_od[row+row_index, col+col_index] = min(stack_od[row+row_index, col+col_index], path[row+row_index][col+col_index].f_dist)
					else:
						stack_od[row+row_index, col+col_index] = path[row+row_index][col+col_index].f_dist


	#This function creates a path through the maze using searchpath function
	def createPath():
		done = Distance.searchPath(mazeStart_X, mazeStart_Y)
		if done:
			print("Maze path is ready")


	#This function searches the path through maze
	def searchPath(currentX, currentY):
		if currentX == mazeEnd_X and currentY == mazeEnd_Y:
			path[currentX][currentY].select = True
			return True
		if path[currentX][currentY].chose:
			path[currentX][currentY].visit = True
			path_right = not maze[currentX][currentY].right and Cell.pointValid(currentX, currentY+1) and not path[currentX][currentY+1].visit
			path_left = not maze[currentX][currentY].left and Cell.pointValid(currentX, currentY-1) and not path[currentX][currentY-1].visit
			path_top = not maze[currentX][currentY].top and Cell.pointValid(currentX-1, currentY) and not path[currentX-1][currentY].visit
			path_down = not maze[currentX][currentY].down and Cell.pointValid(currentX+1, currentY) and not path[currentX+1][currentY].visit

			path[currentX][currentY].select = (path_right and Distance.searchPath(currentX, currentY+1)) or (path_left and Distance.searchPath(currentX, currentY-1)) or (path_top and Distance.searchPath(currentX-1, currentY)) or (path_down and Distance.searchPath(currentX+1, currentY))
			if path[currentX][currentY].select:
				if path_right and path[currentX][currentY+1].select:
					pygame.draw.line(maze_display, (255,0,0), (((currentY+1)*size),((currentX)*size)+(size//2)), (((currentY+1)*size)+(size//2),((currentX)*size)+(size//2)), size//10)
					pygame.draw.line(maze_display, (255,0,0), ((currentY*size)+(size//2),((currentX)*size)+(size//2)), ((currentY*size)+(size),((currentX)*size)+(size//2)), size//10)
				
				elif path_left and path[currentX][currentY-1].select:
					pygame.draw.line(maze_display, (255,0,0), (((currentY-1)*size)+(size//2),((currentX)*size)+(size//2)), (((currentY-1)*size)+(size),((currentX)*size)+(size//2)), size//10)
					pygame.draw.line(maze_display, (255,0,0), (((currentY)*size)+(size//2),((currentX)*size)+(size//2)), ((currentY*size),((currentX)*size)+(size//2)), size//10)
				
				if path_top and path[currentX-1][currentY].select:
					pygame.draw.line(maze_display, (255,0,0), (((currentY)*size)+(size//2),((currentX-1)*size)+(size//2)), ((currentY*size)+(size//2),((currentX-1)*size)+size), size//10)
					pygame.draw.line(maze_display, (255,0,0), ((currentY*size)+(size//2),((currentX)*size)+(size//2)), (((currentY)*size)+(size//2),((currentX)*size)), size//10)
				
				elif path_down and path[currentX+1][currentY].select:
					pygame.draw.line(maze_display, (255,0,0), (((currentY)*size)+(size//2),((currentX+1)*size)+(size//2)), (((currentY)*size)+(size//2),((currentX+1)*size)), size//10)
					pygame.draw.line(maze_display, (255,0,0), ((currentY*size)+(size//2),((currentX)*size)+(size//2)), ((currentY*size)+(size//2),((currentX)*size)+size), size//10)
				# pygame.display.update()
				# pygame.time.delay(50)
			return path[currentX][currentY].select


#Main that calls the initializing function and then maze generator and lastly, maze printer.
if __name__ == '__main__':
	
	#Taking necessary inputs
	
	height = int(input("Maze height:"))
	width = int(input("Maze width:"))
	size = int(input("Cell Size:"))
	print("Possible starting X and end X point are 0 to ", str(width-1))
	print("Possible starting Y and end Y point are 0 to ", str(height-1))
	mazeStart_X = int(input("X coordinate of start point:"))
	mazeStart_Y = int(input("Y coordinate of start point:"))
	mazeEnd_X = int(input("X coordinate of end point:"))
	mazeEnd_Y = int(input("Y coordinate of end point:"))

	if height > 0 and width > 0 and mazeStart_X >= 0 and mazeStart_Y >= 0 and mazeEnd_X <= width-1 and mazeEnd_Y <= height-1 and mazeStart_Y >= 0 and mazeStart_X <= width-1 and mazeStart_Y <= height-1:
		pygame.init()
		maze_display = pygame.display.set_mode((height*size, width*size))
		pygame.display.set_caption('Maze Generator(Recursive Backtracking) and Solver(A* Algorithm)')
		exit = False
		printDone = False

		while not exit:
			if printDone == False:
				#Initialize the maze and search the neibhours by creating a recursive backtracking
				Cell.initializeMaze()
				Cell.routeNeighbour(mazeStart_X, mazeStart_Y)
                
				#Check if all cells are visited
				if Cell.allVisited():
					print("All cells are visited")

				#Initialize the distance, calculate the distances and create a path
				Distance.initializeDist()
				Distance.distCalculation()
				Distance.createPath()

				#Color start and end node to Red
				pygame.draw.rect(maze_display,(0,255,0),((mazeStart_Y*size)+(size//10),(mazeStart_X*size)+(size//10),size-(size//10),size-(size//10)))
				pygame.draw.rect(maze_display,(0,0,255),((mazeEnd_Y*size)+(size//10),(mazeEnd_X*size)+(size//10),size-(size//10),size-(size//10)))
				pygame.display.update()	
				printDone = True
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit = True
		pygame.quit()	

	else:
		print("Out of bound index")	