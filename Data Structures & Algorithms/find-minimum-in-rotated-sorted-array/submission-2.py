class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # sorted
            if nums[l] < nums[r]:
                res = min (res, nums[l])
                break
            # rotated
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                # search right half
                l = m + 1
            else:
                # search left half
                r = m - 1
        return res
