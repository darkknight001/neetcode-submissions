class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def replacements_needed(st, end, d):
            freq = max(d, key=d.get)
            return end-st-d[freq]

        if len(s)==1:
            return 1
        
        ans = 1
        
        seen = {}
        seen[s[0]] = 1
        
        st = 0
        end = 1
        for c in s[1:]:
            # add to seen map
            seen[c]=seen.get(c, 0)+1
            end+=1
            
            # check window violation
            while(replacements_needed(st, end, seen)>k):
                seen[s[st]]-=1
                st+=1
            ans = max(ans, end-st)
        
        return ans
