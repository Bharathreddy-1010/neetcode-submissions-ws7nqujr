class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        # print(n)
        for i in range(0,n-1):
            for j in range(i+1,n):
                # print(nums[i], nums[j])
                if nums[i] == nums[j]:
                    return True
        
        return False       