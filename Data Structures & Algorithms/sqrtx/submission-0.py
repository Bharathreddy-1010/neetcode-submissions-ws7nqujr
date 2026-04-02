class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        ans =0
        while l<=r:
            mid = (l+r)//2

            if mid*mid == x:
                return mid

            if mid*mid>x:
                r = mid-1

            else:
                l = mid+1
                ans = mid
        return ans