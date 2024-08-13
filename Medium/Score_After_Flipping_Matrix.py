
"""
    Information given by default

1) size of the matrix
2) sarting score

objective: maximize the score of the matrix
while minimizing the number of moves (my assumption for optimizing the algorithm)
"""

from typing import List

class Solution:

    def matrixScore(self, grid:List[List[int]]) -> int:
        
        self.m = len(grid)
        self.n = len(grid[0])

        print(self.m, self.n)

    def convert():
        ...


grid = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
sol = Solution
print(sol.matrixScore(grid=grid))