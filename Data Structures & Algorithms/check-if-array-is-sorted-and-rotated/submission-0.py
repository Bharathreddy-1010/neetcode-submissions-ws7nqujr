class Solution:
    def check(self, nums: List[int]) -> bool:
        nums1 = sorted(nums)
        arr = []

        for i in range(0,len(nums)):
            arr.insert(0,nums1.pop())
            if nums == arr+nums1:
                return True

        return False