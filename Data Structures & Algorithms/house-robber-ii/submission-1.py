class Solution:
    def rob(self, nums: List[int]) -> int:
        def helper(nums):
            dp = [0]*(len(nums)+1)
            dp[1] = nums[0]

            for i in range(2, len(nums)+1):
                dp[i] = max(dp[i-2]+nums[i-1], dp[i-1])
            
            return dp[len(nums)]
        
        n = len(nums)
        if n==2:
            return max(nums[0], nums[1])
        if n==1:
            return nums[0]
        
        return max(helper(nums[:-1]), helper(nums[1:]))