# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        le = 0
        re = n

        while le<=re:
            mid = (le+re)//2

            if guess(mid) == 0:
                return mid
            
            elif guess(mid)==-1:
                re=mid-1

            else:
                le = mid+1


        