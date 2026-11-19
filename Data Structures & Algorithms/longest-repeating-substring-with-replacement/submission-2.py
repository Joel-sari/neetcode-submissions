"""
Only given uppercase english characters

"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count_of_char = {} 

        left_p = 0 

        max_char_count = 0

        for right_p, char in enumerate(s): 
            # this dictionary will be dynamic as we scan the string linearly
            count_of_char[char] = count_of_char.get(char, 0) + 1 

            

            # if this happens we need to readjust our window size, if our k isn't enough to skip
            while ((right_p - left_p + 1) - max(count_of_char.values())) > k: 
                count_of_char[s[left_p]] -= 1
                left_p += 1

            max_char_count = max(max_char_count, right_p - left_p + 1)

        return max_char_count 
            
            

                


            

        