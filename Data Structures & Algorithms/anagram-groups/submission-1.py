# This taskes O(m * n)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping character count of each string to list of anagrams

        for s in strs: # go through every word/string
            count = [0] * 26 # one for each character ( a ... z )
            for c in s: # go through every single character of the string
                count[ord(c) - ord("a")] +=1 # counting every character + 1 to update
            res[tuple(count)].append(s) # group all anagrams with that count to the result
        return list(res.values())