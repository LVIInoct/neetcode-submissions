class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            currentsum = numbers[l] + numbers[r]
            if currentsum > target:
                r -= 1 # shift it to the left
            elif currentsum < target:
                l += 1 # shift it to the right
            else:
                return [l + 1, r + 1] # theyre based on 1 so we add 1
        return []