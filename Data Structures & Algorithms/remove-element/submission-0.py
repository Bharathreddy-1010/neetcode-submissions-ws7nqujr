class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        num2 = []
        for i in range(0,len(nums)):
            if nums[i]!=val:
                num2.append(nums[i])
        for i in range(len(num2)):
            nums[i] = num2[i]
        return len(num2)
        
        