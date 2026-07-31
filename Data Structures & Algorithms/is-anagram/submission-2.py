class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t): # if length don't match = not anagram
            return False
        letters = {} # save chars
        for char in s:
            if char in letters:
                letters[char] += 1 # add char
            else:
                letters[char] = 1 # keep it if already in
        for char in t:
            if char in letters: 
               letters[char] -= 1 # remove if its in the hash 
        for count in letters.values():
            if count != 0: # if in the end the list still has items, then t didn't match - not valid anagram
                return False
        return True