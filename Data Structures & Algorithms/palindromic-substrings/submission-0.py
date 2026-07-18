class Solution:
    # Palindrome is basically just tryna see if you can create a 
    # a mirror of itself and the value is still the same. 
    def countSubstrings(self, s: str) -> int:

        """
        BRUTE FORCING! 
        # remember palindrome = two pointers!!!! 

        # We need to generate all possible substrings,
        for each substring check if it is a palindrome
        
        total_palindromes = 0

        # We want the outer loop to go through all the letters in the array  
        for outer_index in range(len(s)):
            # THIS IS IMPORTANT, note the range, it is based off of i, meaning 
            # everythinbg before i has already been seen and counted as a subset, thu we don't need to take it into account 
            for inner_index in range(outer_index, len(s)):
                # NOW NOTiCE HOW WE INTIALIZE LEFT AND RIGHT POINTERS 
                # if they both equal each other (which they will be in our first iteration ), we should automatically count that to our total palindromes
                left_pointer, right_pointer = outer_index, inner_index
                
                # while our pointers don't meet each other/ crossover and the actual characters at the pointers are the same 
                # we can figure decrease/ increase the pointer values. This is is important because as soon as 
                # these pointers overlap, it is a green flag saying that hey this substring completed the palindrome test 
                while left_pointer < right_pointer and s[left_pointer] == s[right_pointer]:
                    left_pointer += 1 
                    right_pointer -= 1

                if left_pointer >= right_pointer: 
                    total_palindromes += 1
        return total_palindromes 
        """

        # The other way is to not have pointers growing outward and subarray growing with it, 
        # for this we will need to take into account two O(n^2) algorithsm in whcih one focuses on 
        # the even substrings and the other focuses on the odd sub strings.


        total_palindromes = 0

        # Okay so we are going to loop throught the whole string s 
        for index in range(len(s)):
            # each new index we want to start both pointer at the same place as the index 
            left_pointer = right_pointer = index
            # This while loop is important!, it checks substrings by expanding both left and right to find valid palindromes for each index 
            # NOTE this gives us the palindroms OF ODD LENGTH
            total_palindromes += self.palindromeCheck(left_pointer, right_pointer, s)


            # NOW WE NEED TO DO THE EVEN SUBSTRING CHECk
            # NOTE: you can do this within the for loop, so you don't have to create a new one, whcih makes sense 
            left_pointer = index 
            right_pointer = index + 1
            total_palindromes += self.palindromeCheck(left_pointer, right_pointer, s)

            # Same thing literally, so that may point us into creating a function to lower the repetition
        return total_palindromes

    def palindromeCheck(self, left_pointer: int, right_pointer: int, s: str):
        total_palindromes = 0
        while left_pointer >= 0 and right_pointer < len(s) and s[left_pointer] == s[right_pointer]:
            total_palindromes+=1
            left_pointer -=1 
            right_pointer +=1
        return total_palindromes
                









        



        