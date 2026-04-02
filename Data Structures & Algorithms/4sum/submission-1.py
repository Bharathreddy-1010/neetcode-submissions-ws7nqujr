class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]

        for i in range(0,n-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            for j in range(i+1,n-2):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
            
                le = j+1
                re = n-1

                while le<re:
                    s = nums[i]+nums[j]+nums[le]+nums[re]

                    if s==target:
                        res.append([nums[i],nums[j],nums[le],nums[re]])

                        le+=1
                        re-=1

                        while le<re and nums[le] == nums[le-1]:
                            le+=1
                        while le<re and nums[re] == nums[re+1]:
                            re-=1
                    elif s<target:
                        le+=1
                    else:
                        re-=1
        return res

