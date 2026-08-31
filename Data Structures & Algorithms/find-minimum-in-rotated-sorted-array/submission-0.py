class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums:
            nums.sort()
            return nums[0]