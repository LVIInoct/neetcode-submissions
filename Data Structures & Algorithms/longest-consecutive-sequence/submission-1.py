# we need to check the following:
# does this number has a left neighbor node? if no: it's the beginning of a new sequence
# does it have a right neighbor node? if no: end the sequence
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # nums is the array numSet is the hash set
        longest = 0
        for i in numSet:
            # check if its the start of a sequence
            if (i - 1) not in numSet:
                length = 0
                while (i + length) in numSet:
                    length += 1 # check one number at a time
                longest = max(length, longest)
        return longest