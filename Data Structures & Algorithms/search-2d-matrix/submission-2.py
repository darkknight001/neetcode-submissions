class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix[0])-1
        t = 0
        b = len(matrix)-1

        row = 0
        found=False
        # out of matrix
        if target<matrix[0][0] or target>matrix[-1][-1]:
            return False

        while(t<=b):
            row = (t+b)//2
            if target<=matrix[row][-1] and target>=matrix[row][0]:
                found = True
                break
            elif target<matrix[row][0]:
                b = row-1
            elif target>matrix[row][-1]:
                t = row+1
    
        if not found:
            return False

        while(l<=r):
            col = (l+r)//2
            if target == matrix[row][col]:
                return True
            elif target< matrix[row][col]:
                r=col-1
            else:
                l=col+1
        
        return False