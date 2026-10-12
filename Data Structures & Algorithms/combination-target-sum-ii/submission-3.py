class Solution:
    def combinationSum2(self, candidates: List[int], t: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        def helper(idx, target, temp):
            if target==0:
                ans.append(temp[:])
                return
            
            if idx>=len(candidates) or target<0:
                return
            
            temp.append(candidates[idx])
            helper(idx+1, target-candidates[idx], temp)
            temp.pop()

            while idx+1<len(candidates) and candidates[idx+1]==candidates[idx]:
                idx+=1
            helper(idx+1, target, temp)
        
        
        helper(0, t, [])
        return ans