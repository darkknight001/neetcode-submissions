class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        elements = set()
        for num in nums:
            elements.add(num)
        ls = 0
        for num in nums:
            if num-1 not in elements:
                cs = 1
                temp = num+1
                while(temp in elements):
                    temp+=1
                    cs+=1
                ls = max(ls, cs)
        
        return ls