class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        
        if s1==s2:
            return True
        l = len(s1)

        freq=Counter(s1)
        for i in range(0, len(s2)-l+1):
            current_seq = s2[i:i+l]
            current_freq=Counter(current_seq)
            if current_freq == freq:
                return True
        
        return False