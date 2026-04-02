class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []

        for token in tokens:
            if token not in  "+-/*":
                res.append(int(token))

            else:
                b = res.pop()
                a = res.pop()

                if token=="+":
                    res.append(a+b)
                elif token == "-":
                    res.append(a-b)
                elif token == "*":
                    res.append(a*b)
                else:
                    cal = int(a/b) if a-b>0 else -(-a//b)
                    res.append(cal)

        return res[0]
