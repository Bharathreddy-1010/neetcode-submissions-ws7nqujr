class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = float("inf")
        l=0
        count = 0
        for r in range(len(nums)):
            count+=nums[r]
            while count>=target:
                minlen=min(minlen,r-l+1)
                count-=nums[l]
                l+=1

        return 0 if minlen==float("inf") else minlen