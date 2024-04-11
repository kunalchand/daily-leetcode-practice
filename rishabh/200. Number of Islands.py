from typing import List
from collections import deque
class Solution:
    '''
    I/O:
        string 2 D array 0 / 1
        no diagonal connection allowed

    egde cases:
    [1 0]
    [0 1] => 2

    Approach:
        O(m * n)

    '''
    ## DFS
    def numIslands(self, grid: List[List[str]]) -> int:

        def dfs(r,c):
            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                grid[r][c] != "1"
                # or (r,c) in visited                                 # no need 
            ):
                return

            grid[r][c] = "-1"                                         # mark
            # visited.add((r,c))                                      # no need
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:         # explore further
                new_r, new_c = r + dr, c + dc
                dfs(new_r, new_c)


        ROWS, COLS = len(grid), len(grid[0])
        count = 0
        # visited = set()                                             # no need
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    count += 1
                    dfs(r,c)

        return count
        

    
    '''
    APPROACH: BFS
    '''
    def numIslands(self, grid: List[List[str]]) -> int: 

        ROWS, COLS = len(grid), len(grid[0])
        island_count = 0
        visited = set()

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                row, col = q.popleft()

                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    new_row, new_col = row + dr, col + dc
                    if (new_row in range(ROWS) and new_col in range(COLS) and 
                        grid[new_row][new_col] == "1" and (new_row, new_col) not in visited):
                        visited.add((new_row, new_col))
                        q.append((new_row, new_col))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)                # for the given (r,c), bfs() will add all the connected cells into visited
                    island_count += 1
        
        return island_count
    
grid = [["1","1","1"],["0","1","0"],["1","1","1"]]
print(Solution().numIslands_bfs(grid))