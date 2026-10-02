class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        pmap = {
            "}":"{",
            "]":"[",
            ")":"(",
        }
        for c in s:
            # opening
            if c not in pmap:
                st.append(c)
                continue

            # closing
            if len(st)==0: 
                return False    
            
            last = st[-1]
            if last!=pmap[c]:
                return False
            st.pop(-1)
        
        return True if not st else False