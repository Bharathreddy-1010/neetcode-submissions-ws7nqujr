class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n= len(nums)
        for i in range(0,n):
            for j in range(i,n):
                if nums[i]>nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
        return nums
        