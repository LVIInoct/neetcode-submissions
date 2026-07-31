class Solution:
# The logic is, we first define how long the word will be using length of s (input) (length int converted to a string) and declare it before s (separated by a delimiter) so we know how much space we'll need to print the word. This is O(n)
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs: # go through the length of input to encode
            res += str(len(s)) + "#" + s # delimiter so we stop counting and then the word itself
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0 # i (pointer) to get start position (0)
        while i < len(s): #while i is still in bounds
            j = i # j as another pointer that will move
            while s[j] != "#":
                j += 1  # while j doesn't point to the delimiter, keep adding until it does
            length = int(s[i:j]) # the length of the string/word starts at i and goes to j (and convert it to a string)
            # now decode starting from delimiter + 1 until delimiter + 1 + length (declared before)
            # and also append it to the result
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length # update so we go to the next word (if there's any)
        return res