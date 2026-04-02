class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for x in nums:
            if x in freq:
                freq[x]+=1
            else:
                freq[x]=1
        points = list(freq.items())
        points.sort(key=lambda x:x[1],reverse = True)

        res = []
        for i in range(0,k):
            res.append(points[i][0])
        return res