class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = {}
        for i, value in enumerate(nums):
            if value in duplicate:
                return True
            duplicate[value] = i
        return False