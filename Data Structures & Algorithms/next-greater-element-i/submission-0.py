class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        n = len(nums2)

        for num in nums1:
            great = -1
            for j in range(n-1,-1,-1):
                if nums2[j]>num:
                    great = nums2[j]

                elif nums2[j]==num:
                    break
            res.append(great)

        return res
