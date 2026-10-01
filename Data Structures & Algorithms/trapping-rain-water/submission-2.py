class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0]*len(height)
        suffix = [0]*len(height)

        maxima = 0
        for i in range(len(height)):
            prefix[i]=max(maxima, height[i])
            maxima = prefix[i]
        
        maxima = 0
        for i in range(len(height)-1, -1, -1):
            suffix[i]=max(maxima, height[i])
            maxima = suffix[i]
        
        water = [0]*len(height)

        for i in range(len(height)):
            water[i] = min(suffix[i], prefix[i]) - height[i]

        return sum(water)