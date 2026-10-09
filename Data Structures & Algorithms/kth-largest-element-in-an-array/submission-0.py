class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = nums[:k]
        heapq.heapify(ans)

        for i in range(k, len(nums)):
            heapq.heappushpop(ans, nums[i])
        
        return ans[0]