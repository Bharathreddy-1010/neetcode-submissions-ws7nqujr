class Solution:
    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1
        while l<r:
            if s[l]!=s[r]:
                skl = s[l+1:r+1]
                skr = s[l:r]

                return skl == skl[::-1] or skr == skr[::-1]
            l +=1
            r-=1
        return True
        
        