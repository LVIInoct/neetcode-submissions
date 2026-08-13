# logic is: as we go through the heights, it needs to be in decreasing order: if the current height is smaller than the next (right) height we first check its max area then we pop it off the stack of heights
# it can be one layer horizontally or vertically like example two, or extend backwards
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair index and height
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: # if previous height is greater than current height
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index)) # i - index is width, calculate area x width this with every pop
                start = index #update
            stack.append((start, h))
        # for numbers that extend all the way to the end of the histogram
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i)) # area x width
        return maxArea