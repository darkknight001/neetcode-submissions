class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        
        while(l<=r):
            mid = (l+r)//2
            print("checking ", nums[mid])
            if nums[mid]>=nums[0] and target<nums[0]:
                l = mid+1
            elif nums[mid]<nums[0] and target>=nums[0]:
                r = mid-1
            else:
                if nums[mid]<target:
                    l = mid+1
                elif nums[mid]>target:
                    r = mid-1
                else:
                    return mid
        
        return -1