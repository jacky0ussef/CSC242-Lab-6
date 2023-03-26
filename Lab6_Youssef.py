'''
Jack Youssef
3/8/2023

Contains the main driver function, which completes a Maze.

The function opens the input file, reads it, and copies the contents into a list.
Then, an empty Grid is created and updated with the contents of the list, with an extra for the solution.
The function then utilizes an ArrayStack to iterate through the maze, mark its path, and use backtracking to find a solution.

If a path is found, it is displayed, copied into a solution file, then the original maze is shown once more.
Otherwise, the user is informed that the maze has no solution.

Other files: arrays.py, grid.py, maze1.maz(input), solution.txt(output).
'''

from grid import Grid
from arraystack import ArrayStack

def main():
    ''' Main driver function. Takes a "Maze" file (maze1.maz), displays the maze,
    attempts to find a solution, displays the result, displays the maze once more, 
    then writes the solution of the original input maze to a file called solution.txt. '''

    # opens file, copies contents, and initiates maze Grid
    with open('maze1.maz', 'r') as infile:
        rows = 0
        grid_queue = []
        for line in infile:
            #print(line, end="")
            rows += 1
            copy = str(line).strip()
            grid_queue.append(copy)
        columns = len(line) 
                                                    
        maze = Grid(rows, columns)
        maze_solution = Grid(rows, columns)
    
    # updates contents of Grid
    row_index = 0
    for row in grid_queue:
        column_index = 0
        for item in row:
            if item == 'P':
                start = [row_index, column_index]  # marking start position
            maze[row_index][column_index] = item
            maze_solution[row_index][column_index] = item
            column_index += 1
        row_index += 1

    # display maze
    print('Maze:\n')
    print(maze)
    
    # find solution, if possible
    path = ArrayStack()
    path.push(start)
    while len(path) != 0:
        current = path.pop()
        if maze_solution[current[0]][current[1]] == 'T':
            print('Solution:\n')
            found = True
            break
        elif maze_solution[current[0]][current[1]] != '.':
            maze_solution[current[0]][current[1]] = '.'
            for top in range(-1, 2):
                if maze_solution[current[0] - 1][current[1] + top] != ('*' or '.'):
                    path.push([current[0] - 1, current[1] + top])
            if maze_solution[current[0]][current[1] - 1] != ('*' or '.'):
                    path.push([current[0], current[1] - 1])
            if maze_solution[current[0]][current[1] + 1] != ('*' or '.'):
                    path.push([current[0], current[1] + 1])         
            for bottom in range(-1, 2):
                if maze_solution[current[0] + 1][current[1] + bottom] != ('*' or '.'):
                    path.push([current[0] + 1, current[1] + bottom])  
    if len(path) == 0:
        print('No solution found!')
        found = False    

    # prints solution, if exists, and outputs to file
    if found:
        print(maze_solution)
        print('Original maze:\n')
        print(maze)
    
        with open('solution.txt', 'w') as outfile:
            outfile.write(str(maze_solution))


if __name__ == '__main__': 
    main()
    
