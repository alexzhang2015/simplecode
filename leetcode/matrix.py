from typing import List
from typing import Optional

class Solution:
    # https://leetcode.cn/problems/set-matrix-zeroes/description/?envType=study-plan-v2&envId=top-100-liked
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = set()
        cols = set()
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in rows or j in cols:
                    matrix[i][j] = 0
    
    # 岛屿类问题的通用解法、DFS 遍历框架
    # https://leetcode.cn/problems/number-of-islands/description/?envType=study-plan-v2&envId=top-100-liked
    # https://leetcode.cn/problems/number-of-islands/?envType=study-plan-v2&envId=top-100-liked
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != '1':
                return
            grid[row][col] = '0'
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    count += 1
                    dfs(row, col)

        return count
    
    # https://leetcode.cn/problems/island-perimeter/
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        perimeter = 0

        visited = set()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or grid[r][c] == 0:
                return

            visited.add((r, c))

            if r == 0 or grid[r-1][c] == 0:
                nonlocal perimeter
                perimeter += 1

            if r == rows - 1 or grid[r+1][c] == 0:
                perimeter += 1

            if c == 0 or grid[r][c-1] == 0:
                perimeter += 1

            if c == cols - 1 or grid[r][c+1] == 0:
                perimeter += 1

            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c)

        return perimeter
