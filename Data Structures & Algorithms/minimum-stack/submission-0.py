class MinStack:

    def __init__(self):
        self.st = []
        self.ms = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.ms or self.ms and val<=self.ms[-1]:
            self.ms.append(val)

    def pop(self) -> None:
        val = self.st.pop(-1)
        if val==self.ms[-1]:
            self.ms.pop(-1)

    def top(self) -> int:
        return self.st[-1]
        

    def getMin(self) -> int:
        return self.ms[-1]
        
