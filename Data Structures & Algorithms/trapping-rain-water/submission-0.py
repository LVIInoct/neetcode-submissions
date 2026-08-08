# need max height on both L and R and see if there could be water
# min of the L and R - height [i] to determine how much water we can fit there
# if its 0 or below then we cant fit
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0 # if empty
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l+=1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res