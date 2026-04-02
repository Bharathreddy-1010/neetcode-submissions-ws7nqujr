class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        hashh = {0:1}
        for num in nums:
            prefix+=num
            if prefix-k in hashh:
                count+=hashh[prefix-k]

            if prefix in hashh:
                hashh[prefix]+=1
            else:
                hashh[prefix]=1

        return count

