class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        ans = []
        def helper(idx, word):
            if idx==len(digits):
                ans.append(word)
                return
        
            for c in keypad[digits[idx]]:
                helper(idx+1, word+c)
        if not digits:
            return []
        helper(0, "")

        return ans

