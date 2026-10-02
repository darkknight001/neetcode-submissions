class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currentLength = 0
        maxLength = 0
        unique = set()
        st = 0
        end = 0
        for c in s:
            if c not in unique:
                end+=1
                unique.add(c)
                currentLength+=1

            else:
                maxLength = max(maxLength, currentLength)
                while(st<end):
                    if s[st]!=c:
                        unique.remove(s[st])
                        currentLength-=1
                        st+=1
                
                    else:
                        st+=1
                        end+=1
                        # currentLength = end-st
                        maxLength = max(maxLength, currentLength)
                        break
        
        return max(currentLength, maxLength)
                        