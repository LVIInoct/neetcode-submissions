# Need postfix and prefix
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        prefix = 1 # initial prefix of 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) -1, -1, -1): # reverse order
            res[i] *= postfix
            postfix *= nums[i]
        return res