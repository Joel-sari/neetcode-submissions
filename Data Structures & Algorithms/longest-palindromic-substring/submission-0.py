"""
Th ]e algorithm to solve this is by using two poimters startimng from the 
center fo a character, and moving outwarsd and comparing the characters 
as we move outwards and seeing if they match

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        pailndromy = ""

        # Palindrome length keeps track of the longest alindorm 
        palindrome_length = 0

        for index in range(len(s)):

            #First we are going to check odd length palindromes!
            # we have both pointers start on the index valey
            left_pointer, right_pointer = index, index

            # we then loop while we are in bounds AND if pointe rleftpointer and right pointer equal eachother
            while left_pointer >= 0 and right_pointer < len(s) and s[left_pointer] == s[right_pointer]:
                if (right_pointer - left_pointer + 1) > palindrome_length:
                    palindromy = s[left_pointer:right_pointer + 1]
                    palindrome_length = (right_pointer - left_pointer + 1)

                #Shifting our pointers outwards to go throygh the rest of the string
                left_pointer -= 1
                right_pointer +=1
            
            #EVEN LENGTH PALNDROME CHECK, we update the index values to now have one target 
            # the intial + instead of the same one. BASICALLY WE CHECK AT THE SMALLEST BEING 2 Characters long 
            #INSTEAD OF THE ODD WHERE WE STARTED AT 1 CHARECTER.
            left_pointer, right_pointer = index, index + 1
            while left_pointer >= 0 and right_pointer < len(s) and s[left_pointer] == s[right_pointer]:
                if (right_pointer - left_pointer + 1) > palindrome_length:
                    palindromy = s[left_pointer : right_pointer + 1]
                    palindrome_length = right_pointer - left_pointer + 1
                
                #U[date our pointers the same way 
                left_pointer -= 1
                right_pointer += 1
        return palindromy

            



        
        