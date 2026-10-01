class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars = {}
        for c in s:
            chars[c] = chars[c]+1 if c in chars.keys() else 1
        
        for ch in t:
            if ch not in chars.keys():
                return False
            
            chars[ch]-=1
            if chars[ch]==0:
                del chars[ch]
        
        if chars:
            print(chars)
            return False

        return True