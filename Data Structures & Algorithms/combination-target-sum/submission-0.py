class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []
        def helper(idx, target, temp):
            if idx==len(nums):
                return
            
            if target==0:
                self.ans.append([*temp])
                return
            if target>=nums[idx]:
                temp.append(nums[idx])
                helper(idx, target-nums[idx], temp)
                temp.pop()
            helper(idx+1, target, temp)
        helper(0, target, [])

        return self.ans