class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''l = 0
        r = len(nums)-1

        while l<=r:
            if nums[l]>nums[r]:
                nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1

        return nums'''
        nums.sort()

            