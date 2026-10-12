class MedianFinder:

    def __init__(self):
        self.lh = []
        self.uh = []
        heapq.heapify(self.uh)
        heapq.heapify(self.lh)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lh, -num)
        heapq.heappush(self.uh, -heapq.heappop(self.lh))

        if len(self.uh)> len(self.lh):
            heapq.heappush(self.lh, -heapq.heappop(self.uh))

    def findMedian(self) -> float:
        if len(self.lh)==len(self.uh):
            return (self.uh[0]-self.lh[0])/2
        
        return -self.lh[0]
        