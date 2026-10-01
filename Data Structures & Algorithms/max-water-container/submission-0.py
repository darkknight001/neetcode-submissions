class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxwater = 0
        l = 0
        r = len(heights)-1
        
        while(l<=r):
            area = min(heights[r],heights[l])*(r-l)
            maxwater = max(maxwater, area)
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        return maxwater