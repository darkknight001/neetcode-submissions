class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []
        for c in s:
            if c.isalnum():
                cleaned.append(c)

        i = 0
        j = len(cleaned)-1
        cleaned = "".join(cleaned).lower()
        # while(i<j):
        #     if cleaned[i] == cleaned[j]:
        #         j-=1
        #         i+=1
        #     else:
        #         return False
        
        # return True
        return cleaned[::-1]==cleaned