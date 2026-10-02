class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        mheap = []
        heapq.heapify(mheap)

        for i in range(k):
            heapq.heappush(mheap, (-nums[i], i))
        
        ans.append(-mheap[0][0])

        if len(nums)==k:
            return ans

        for i in range(k, len(nums)):
            inc = nums[i]
            exc = nums[i-k]
            
            heapq.heappush(mheap, (-inc, i))
            while mheap[0][1]<=i-k:
                heapq.heappop(mheap)
            
            ans.append(-mheap[0][0])

        return ans