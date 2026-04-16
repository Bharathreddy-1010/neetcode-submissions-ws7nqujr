class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res =0
        for w in words:
            count =1
            for i in w:
                if i not in allowed:
                    count =0
                    break

            res+=count

        return res 