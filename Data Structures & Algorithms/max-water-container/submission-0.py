class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            area = ( r - l ) * min(heights[l], heights[r]) # calculate area
            res = max(res, area)
            if heights[l] < heights[r]: # if l is min, shift it. we could make one for r but else does it already
                l += 1
            else:
                r -= 1 # in case they're the same
        return res