class TimeMap:

    def __init__(self):
        self.keymap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keymap:
            self.keymap[key]=[]

        self.keymap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        def bs(values, ts):
            l = 0
            r = len(values)-1
            res=""
            while(l<=r):
                mid = (l+r)//2
                tsm = values[mid][0]
                if tsm<=ts:
                    res = values[mid][1]
                    l = mid+1
                else:
                    r = mid-1
            return res
        
        if key not in self.keymap:
            return ""
        values = self.keymap[key]
        return bs(values, timestamp)        
