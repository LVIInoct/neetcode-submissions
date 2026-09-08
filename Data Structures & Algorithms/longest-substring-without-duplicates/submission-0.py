class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        # In sliding window, R keeps moving.
        l = 0
        res = 0
        for r in range(len(s)):
            # while there's still a duplicate:
            while s[r] in charset:
                charset.remove(s[l])
                # move window to the right
                l += 1
            charset.add(s[r])
            res = max(res, r - l + 1)
        return res