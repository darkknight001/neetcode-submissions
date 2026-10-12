class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort()
        def helper(idx, ssf):
            if len(nums)==idx:
                self.ans.append([*ssf])
                return
            
            ssf.append(nums[idx])
            helper(idx+1, ssf)
            ssf.pop()
            while(idx+1<len(nums) and nums[idx+1]==nums[idx]):
                idx+=1
            helper(idx+1, ssf)
        
        helper(0, [])
        return self.ans