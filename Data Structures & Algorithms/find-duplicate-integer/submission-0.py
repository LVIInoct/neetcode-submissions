# sort the array so duplicates are next to each other
# a value will point to an index of its value ONCE, more than that it's a cycle
# no value will point at index 0 in the detection of a cycle
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort() # sort for binary search
        for i in range (len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        return -1
            