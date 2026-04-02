class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans  = [0]*len(arr)
        for i in range(0,len(arr)):
            right = -1
            for j in range(i+1,len(arr)):
                right = max(arr[j],right)

            ans[i] = right

        return ans