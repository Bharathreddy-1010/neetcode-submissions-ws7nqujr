class Solution:
    def largestGoodInteger(self, num: str) -> str:
        con = ""
        for i in range(len(num)-2):
            if num[i]==num[i+1]==num[i+2]:
                con = max(con,num[i])

        return con*3 if con else ""

