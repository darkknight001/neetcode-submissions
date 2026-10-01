class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        1. No rows should have same number twice
        2. No columns should have same number twice
        3. No 3x3 box should have same number twice
        """
        # row check
        for row in board:
            seen = set()
            for element in row:
                if element == ".":
                    continue
                if element in seen:
                    return False
                seen.add(element)
        
        # Column check
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col]==".":
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col]) 
        
        # block check
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                seen = set()
                for row in range(box_row, box_row+3):
                    for col in range(box_col, box_col+3):
                        if board[row][col]==".":
                            continue

                        if board[row][col] in seen:
                            print("box failed")
                            return False
                        seen.add(board[row][col])
            
        return True