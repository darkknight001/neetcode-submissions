class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        ans = 0
        for i in range(len(heights)):
            start = i
            while st and st[-1][1]>heights[i]:
                idx, height = st.pop()
                ans = max(ans, height*(i-idx))
                start = idx
            st.append((start, heights[i]))
        

        for i, h in st:
            ans = max(ans, h*(len(heights)-i))
        return ans
        
