class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            left = right = 0
            for l in range(i):
                left +=nums[l]

            for r in range(i+1,n):
                right+=nums[r]

            if left == right:
                return i
        return -1
