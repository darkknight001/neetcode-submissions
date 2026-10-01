class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}

        for i, num in enumerate(nums):
            diff[num] = i

        for i, num in enumerate(nums):
            tar = target-num
            if tar in diff.keys() and diff[tar]!=i:
                return [i, diff[tar]]
