class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_set = set() 

        left_p = 0

        longest_substring = 0
    
        for right_p, character in enumerate(s): 
            
            while character in string_set: 
                string_set.remove(s[left_p])
                left_p += 1 
            longest_substring = max(longest_substring, right_p - left_p + 1)
            string_set.add(character)

        return longest_substring
                


        