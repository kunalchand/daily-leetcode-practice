from typing import List

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
        