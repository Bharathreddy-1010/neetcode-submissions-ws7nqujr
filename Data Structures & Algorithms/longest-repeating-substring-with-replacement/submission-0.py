class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxele = 0
        maxlen = 0
        hashh = [0]*26
        l = 0

        for r in range(len(s)):
            idx = ord(s[r])-ord("A")
            hashh[idx]+=1
            maxele = max(maxele,hashh[idx])
            window = r-l+1

            if window-maxele>k:
                hashh[ord(s[l])-ord("A")]-=1
                l+=1

            maxlen = max(maxlen,r-l+1)
        
        return maxlen