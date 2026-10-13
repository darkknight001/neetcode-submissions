class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        visited = [[0]*cols for _ in range(rows)]
        self.ans = False

        def backtrack(idx, r, c):
            if idx==len(word):
                return True

            if r<0 or c<0 or r>=rows or c>=cols:
                return False
            
            if visited[r][c] or board[r][c]!=word[idx]:
                return False
            
            visited[r][c]=1
            found = (backtrack(idx+1, r+1, c) or
                     backtrack(idx+1, r-1, c) or
                     backtrack(idx+1, r, c+1) or
                     backtrack(idx+1, r, c-1))
            visited[r][c]=0
            return found

        for r in range(rows):
            for c in range(cols):
                if backtrack(0, r, c):
                    return True

        return False