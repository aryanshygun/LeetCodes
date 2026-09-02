# https://www.codewars.com/kata/5296bc77afba8baa690002d7/solutions/python?filter=me&sort=best_practice&invalids=false

def is_valid(grid, row, col, num):
    
    # check if in row
    if num in grid[row] or num in [grid[i][col] for i in range(9)]:
        return False
    
    # check if in column
    # if num in [grid[i][col] for i in range(9)]:
    #     return False
    
    # check if in the cubicle
    startrow = 3 * (row // 3)
    startcol = 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[startrow + i][startcol + j] == num:
                return False              
    # if the num wasnt in neither row col or cubicle        
    else:
        return True
    
def zerocell(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return i, j
    return None, None    
            
def sudoku(grid):
    
    # if there are no epty spaces
    row, col = zerocell(grid)
    if row is None and col is None:
        return True
    
    # back track method in ordre to place 
    for num in range(1, 10):
        if is_valid(grid, row, col, num):
            grid[row][col] = num
            
            if sudoku(grid):
                return grid
            
            # if the num added doesnt add up
            grid[row][col] = 0
            
    # if the sudoku doesnt get fixed
    return False