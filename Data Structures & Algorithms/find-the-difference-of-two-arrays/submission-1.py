class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res1 = []
        res2 = []
        for i in range(len(nums1)):
            if nums1[i] not in nums2 and nums1[i] not in res1:
                res1.append(nums1[i])
        for j in range(len(nums2)):
            if nums2[j] not in nums1 and nums2[j] not in res2:
                res2.append(nums2[j])

        return [res1,res2]