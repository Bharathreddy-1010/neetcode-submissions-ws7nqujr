class Solution:
    def isValid(self, s: str) -> bool:
        st =[]
        for i in range(0,len(s)):

            if s[i] == "(" or s[i]=="[" or s[i]=="{":
                st.append(s[i])

            elif s[i]==")":
                if not st or st[-1]!= "(":
                    return False
                st.pop()

            elif s[i] == "}":
                if not st or st[-1]!= "{":
                    return False
                st.pop()

            elif s[i] == "]":
                if not st or st[-1]!= "[":
                    return False
                st.pop()

        if len(st)==0:
            return True
        else:
            return False
            
            
