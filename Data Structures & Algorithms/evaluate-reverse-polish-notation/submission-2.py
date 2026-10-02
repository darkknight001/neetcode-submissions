class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                st.append(int(token))
            else:
                n2 = int(st.pop(-1))
                n1 = int(st.pop(-1))
                res=None
                if token == "+":
                    res = n1+n2
                elif token == "-":
                    res = n1-n2
                elif token == "*":
                    res = n1*n2
                else:
                    res = int(n1/n2)
                
                st.append(res)
        
        return int(st[-1])