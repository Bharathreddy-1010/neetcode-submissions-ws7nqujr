class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        res = 0
        for r in range(len(s)-1,-1,-1):
            if s[r]==" ":
                break
            
            res+=1
        return res



