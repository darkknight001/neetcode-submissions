class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        result = [0]*len(temperatures)
        for i in range(len(temperatures)):
            if not st or temperatures[st[-1]]>=temperatures[i]:
                st.append(i)
            else:
                while(st and temperatures[i]>temperatures[st[-1]]):
                    idx = st.pop(-1)
                    result[idx] = i-idx
                st.append(i)

        return result

            