class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while(len(stones)>1):
            f = heapq.heappop(stones)
            s = heapq.heappop(stones)
            rem = abs(f-s)
            if rem:
                heapq.heappush(stones,-rem)
            
        return -stones[0] if stones else 0
