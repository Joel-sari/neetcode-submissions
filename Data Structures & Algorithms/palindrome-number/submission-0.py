class Solution:
    def isPalindrome(self, x: int) -> bool:
        string_format_x = str(x)
        left_pointer, right_pointer = 0, len(string_format_x)-1

        

        while left_pointer < right_pointer: 
            if string_format_x[left_pointer] != string_format_x[right_pointer]:
                return False 
            left_pointer += 1
            right_pointer -= 1
            



        return True
        