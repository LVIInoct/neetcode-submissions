class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum()) # make the string ignore all spaces and ponctuation
        if s == s[::-1]: # compare string to reversed string
            return True
        return False