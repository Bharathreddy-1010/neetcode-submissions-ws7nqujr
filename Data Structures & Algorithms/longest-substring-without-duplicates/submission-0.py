class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        r = 0
        max_len = 0
        hashh = [-1] * 256

        while r<len(s):
            if hashh[ord(s[r])]!=-1:
                if hashh[ord(s[r])]>=l:
                    l = hashh[ord(s[r])]+1
            length = r-l+1
            max_len = max(length,max_len)

            hashh[ord(s[r])] = r
            r+=1
        return max_len 
