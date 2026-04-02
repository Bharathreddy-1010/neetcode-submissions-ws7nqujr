class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        count = [0]*26

        for c in s:
            count[ord(c) - ord('a')]+=1
        
        for d in t:
            count[ord(d) - ord('a')]-=1

        for ch in count:
            if ch != 0:
                return False
        return True
        