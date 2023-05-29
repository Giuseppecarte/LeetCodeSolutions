''' Valid Sudoku

- Runtime: 512 ms 

- Memory Usage: 33 MB

        Subission Results 

- Runtime better than 5.36% of the total submissions 

- Memory better than 6.80% of total submissions

'''
import numpy as np
from typing import List

class Solution:
    def is_valid(self, board: np.array, axis: int=1) -> bool:
        board = board if axis == 0 else board.T
        for index in range(board.shape[0]):
            row = board[index,:]
            raw_row, _ = np.unique(np.delete(row, np.where(row == '.')), return_counts = True)
            if list(filter(lambda x : True if x > 1 else False, _ )):
                return False
        return True


    def valid_subsquares(self, board: np.array) -> bool:
        blocks = [0,3,6,9]
        for i in range(1,len(blocks)):
            for j in range(1,len(blocks)):
                previous_row = blocks[i-1]
                current_row = blocks[i]
                
                previous_col = blocks[j-1]
                current_col = blocks[j]

                sub_square = board[previous_row:current_row, previous_col:current_col].flatten()
                _, counts = np.unique(np.delete(sub_square, np.where(sub_square == '.')), return_counts = True)
                if list(filter(lambda x : True if x > 1 else False, counts )):
                    return False
        return True
    

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board = np.array(board)

        valid_rows = self.is_valid(board, axis = 0)
        valid_columns = self.is_valid(board, axis = 1)

        if valid_rows and valid_columns:
            return self.valid_subsquares(board)

        else: return False


print(Solution().isValidSudoku(board2))