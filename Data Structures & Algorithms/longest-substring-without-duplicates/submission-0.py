class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        left_p = 0
        res = 0
        for right_p in range(len(s)):
            while s[right_p] in charSet:
                charSet.remove(s[left_p])
                left_p+=1
            charSet.add(s[right_p])
            res = max(res, right_p - left_p + 1)
        return res


        