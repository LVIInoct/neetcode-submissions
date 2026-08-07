# sort the array first then eliminate duplicates as we first declare A
# then use two sum II pointers (sum > 0 then move right - 1 or sum < 0 then move left + 1)
# total is O(n²) time and sorting O(1)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums): # go through nums for a first value
            if i > 0 and a == nums[i - 1]: # if i > 0 (so it can't be the first value) & if it's the same as its left neighbor
                continue # since it's a duplicate we skip it

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1 # update left
                    while nums[l] == nums[l - 1] and l < r: # if left becomes duplicate too
                        l += 1 # move it past the duplicate
        return res