class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def helper(idx, ssf):
            if len(nums)==idx:
                self.ans.append([*ssf])
                return
            
            helper(idx+1, ssf)
            ssf.append(nums[idx])
            helper(idx+1, ssf)
            ssf.pop()
        
        helper(0, [])
        return self.ans