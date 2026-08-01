# Todo
# - Declare hash map where we'll count frequency
# - Check nums size and make an input array (bucket) of that size + 1
# - In that array: values are the numbers inside nums and keys are how many times it shows up
# - Ex.: nums has the number 1 three times. assign it inside the array to key 3 (3 contains [1]). if another number like 2 also appears three times assign it to 3 ([1, 2]). if 3 appears 2 times assign it to 2 (2 contains [3])
# - Check bucket elements in descending order as we only want the K amount of max values
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # count number frequency
        freq = [[] for n in range(len(nums) + 1)] # array for bucket sorting + size

        for n in nums: # go through nums
            count[n] = 1 + count.get(n, 0) # counts numbers. if it doesn't exist set it to default 0
        for n, c in count.items(): # returns key-value pair for every (n)umber and (c)ount
             freq[c].append(n) # this value N occurs C amount of times

        res = [] # define result list
        for i in range(len(freq) - 1, 0, -1): # go in descending order through the length of freq array
            for n in freq[i]: # go through array
                res.append(n) # append it to the result
                if len(res) == k: # stop counting descending when the length/values of res is K amount
                    return res