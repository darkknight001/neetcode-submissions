class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        
        buckets = [[] for _ in range(len(nums))]

        for key,val in freq.items():
            buckets[val-1].append(key)
        
        ans = []
        i  = 0
        for bucket in reversed(buckets):
            if i==k:
                break

            if bucket:
                if len(bucket)<=k-i:
                    ans.extend(bucket)
                    i+=len(bucket)
                else:
                    ans.extend(bucket[:k-i])
                    i+=k-i
        return ans