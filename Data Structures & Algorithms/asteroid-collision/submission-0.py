class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []

        for s in asteroids:
            alive = True

            while alive and st and st[-1]>0 and s<0:
                if st[-1]<abs(s):
                    st.pop()
                    continue
                elif st[-1] == abs(s):
                    st.pop()
                    alive = False

                else:
                    alive = False
            if alive:
                st.append(s)

        return st