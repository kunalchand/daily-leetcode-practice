"""
1886. Determine Whether Matrix Can Be Obtained By Rotation

Given two n x n binary matrices mat and target, 
return true if it is possible to make mat equal to 
target by rotating mat in 90-degree increments, or false otherwise.

Example 1:
    Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
    Output: true
    Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.

Example 2:
    Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
    Output: false
    Explanation: It is impossible to make mat equal to target by rotating mat.

Example 3:
    Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
    Output: true
    Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.

Constraints:
    N/A
"""

# 4 * O(rotation) + O(comparison) => O(n ** 2)

# transposing + reversing => rotated()
# compare

# mat[i][j] <=> mat[j][i]

from typing import List
class Solution:
    def transpose_mat(self, mat: List[List[int]]) -> None:
        for r in range(self.n):
            for c in range(self.n):
                if r != c:
                    mat[r][c], mat[c][r] = mat[c][r], mat[r][c]


    def reverse_mat(self, mat: List[List[int]]) -> None:
        for r in range(self.n):
            mat[r] = reversed(mat[r])

    def rotate_mat(self, mat: List[List[int]]) -> None:
        self.transpose_mat(mat)
        self.reverse_mat(mat)

    def compare_mat(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        return mat == target

    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        self.n = len(mat)
        for _ in range(5):
            self.rotate_mat(mat)
            if self.compare_mat(mat, target): 
                return True

        return False