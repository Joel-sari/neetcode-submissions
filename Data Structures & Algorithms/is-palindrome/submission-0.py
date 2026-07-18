class Solution:
    def isPalindrome(self, s: str) -> bool:

        newString = ""
        for character in s:
            if character.isalnum():
                newString += character.lower()
        return newString == newString[::-1] # This a splicing strategy that reverses a string
        # Palindrome is a string that reads the same forward and backward
        """
        My own Solution
            if len(s) < 2:
                return False

            stringy = ""

            for char in s:
                if char == " " or char == "?":
                    continue
                stringy += char.lower()

            
            
            reversing = stringy[::-1] # this is reversing

            if reversing == stringy:
                return True 
            return False

        c.isalnum() # an alpha numerical function that checks if the character is a letter or number only (so it doesn't include other special characters)

        """

    

    
        
        