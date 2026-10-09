class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.store = [*nums]
        self.size = k
        heapq.heapify(self.store)
        self._maintain()

    def _maintain(self):
        while(len(self.store)>self.size):
            heapq.heappop(self.store)

    def add(self, val: int) -> int:
        heapq.heappush(self.store, val)
        self._maintain()
        return self.store[0]
        
