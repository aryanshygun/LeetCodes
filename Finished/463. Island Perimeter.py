# https://leetcode.com/problems/island-perimeter/?envType=daily-question&envId=2024-04-18

class Solution:
    def islandPerimeter(self, grid) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])
        
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 1:
                    perimeter += 4
                    if r > 0 and grid[r-1][c] == 1:
                        perimeter -= 2
                    if c > 0 and grid[r][c-1] == 1:
                        perimeter -= 2
                        
        return perimeter
    
x = Solution()

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

print(x.islandPerimeter(grid))