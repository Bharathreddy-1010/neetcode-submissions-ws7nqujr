class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)

        for i in range(n):
            pro = 1
            for j in range(n):
                if i == j:
                    continue
                
                pro*=nums[j]

            res.append(pro)
        return res