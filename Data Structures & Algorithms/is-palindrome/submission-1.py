class Solution:
    def isPalindrome(self, s: str) -> bool:
        left_p, right_p = 0, len(s) - 1 

        while left_p < right_p: 
            while left_p < right_p and not s[left_p].isalnum():
                left_p += 1
            while left_p < right_p and not s[right_p].isalnum():
                right_p -= 1

            if s[left_p].lower() != s[right_p].lower(): 
                return False

            left_p +=1 
            right_p-= 1

           
        return True
        