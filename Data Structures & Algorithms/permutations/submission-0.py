class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def helper(idx): 
            if len(nums)==idx:
                ans.append(nums[:])
                
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                helper(idx+1)
                nums[idx], nums[i] = nums[i], nums[idx]
        
        helper(0)
        
        return ans