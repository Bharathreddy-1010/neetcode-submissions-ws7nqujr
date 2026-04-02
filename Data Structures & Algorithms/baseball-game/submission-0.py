class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for i in range(len(ops)):
            if ops[i] not in "+CD":
                res.append(int(ops[i]))
            elif ops[i]=="+":
                res.append(res[-2]+res[-1])
            elif ops[i]=="C":
                res.pop()
            else:
                res.append(res[-1]*2)
        return sum(res)
