class Solution:
    def maxArea(self, heights: List[int]) -> int:
        le = 0
        re  = len(heights)-1
        max_area = 0

        while le < re:
            distance = re -le
            min_height = min(heights[le],heights[re])

            area = min_height * distance

            if max_area<area:
                max_area = area


            if heights[le]<heights[re]:
                le+=1

            else:
                re-=1
        return max_area
