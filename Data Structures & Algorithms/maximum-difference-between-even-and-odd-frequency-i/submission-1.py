class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0)+1

        even = float("inf")
        odd = 0
        for values in freq.values():
            if values%2==0:
                even = min(even,values)

            else:
                odd = max(values,odd)

        return odd - even