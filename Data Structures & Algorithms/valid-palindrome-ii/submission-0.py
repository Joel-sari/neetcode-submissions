class Solution:
    def validPalindrome(self, s: str) -> bool:
        left_p, right_p = 0, len(s) - 1

        while left_p < right_p:
            if s[left_p] != s[right_p]:
                # The syntax to deleting/passing over a string in existing s is 
                # We are basically just slicing!!!! Notice this a very impotant skill to hav in python
                skip_left_char = s[left_p+ 1 : right_p + 1] # We use r + 1 to include the last character else it wont include it
                skip_right_char = s [left_p : right_p] # stops at r - 1 thus doesn't include the charcater at position r 

                # Now we want to return to see if after deleting the character the string becomes a palindrom
                # Palindrome is said to be good if you can reverse the string and it equals the original s,
                # In this case we will be comparing with the modified/ skipped character string 

                return skip_left_char == skip_left_char[::-1] or skip_right_char == skip_right_char[::-1]

            # in the case that we don't encounter two characters that aren't equal we can just 
            # update the pointer values and continue on checking in s array.
            left_p +=1 
            right_p -=1

        return True





        