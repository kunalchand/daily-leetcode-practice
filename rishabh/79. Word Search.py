from typing import List

class Solution:
    '''
    I:
        matrix (m x n) with string ele, word (str)
    O:
        bool
    clarifying ques:
        value for m and n 1 to 6
        word len  1 to 15
        lower case/upper case

        ["A"], word = "ABC" => False

    APPROACH:
        1. 
        up, down, left, right => valid moves
        
    Time Complexity:    
        (n * m) * 3 * (k * arbitary paths),        k : word length
        OR
        (n * m) * 3 ^ (k)
        only 3 paths from a given point


    '''
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack_dfs_OR(row, col, i):
            if i == len(word):
                return True
            
            if (
                row not in range(ROWS) or
                col not in range(COLS) or
                board[row][col] != word[i] or
                (row, col) in path
            ):
                return False
            
            path.add((row, col))
            res =   backtrack_dfs_OR(row + 1, col, i + 1) or \
                    backtrack_dfs_OR(row - 1, col, i + 1) or \
                    backtrack_dfs_OR(row, col + 1, i + 1) or \
                    backtrack_dfs_OR(row, col - 1, i + 1)
            path.remove((row, col))

            return res

        def backtrack_dfs(row, col, i):

            if i == len(word):
                return True

            # check if given idx is inbounds and not in visited
            if (
                row not in range(ROWS) or
                col not in range(COLS) or
                (row, col) in path or
                board[row][col] != word[i]
            ):
                return False

            #               down      up      left    right 
            for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                path.add((row, col))                                    
                if backtrack_dfs(row + dr, col + dc, i + 1):
                    return True
                path.remove((row, col))
                    

        ROWS, COLS = len(board), len(board[0])
        if len(word) > ROWS * COLS:                            # if board doesn't contaiin enough letters
            return False

        # to make sure that I don't check the last cell in the path (or go backwards) 
        # eg : grid = AB, word = ABA shouldn't return True
        path = set()

        for r in range(ROWS):
            for c in range(COLS):
                # if backtrack_dfs(r, c, 0):                     # backtracking step
                if backtrack_dfs_OR(r, c, 0):                    # backtracking step
                    return True
        return False


        # prob : should only go to direction where it's not coming from
        # sol: visited()


# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word = "ABCCED"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"

print(Solution().exist(board, word))