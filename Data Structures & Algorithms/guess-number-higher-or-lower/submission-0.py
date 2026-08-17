# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lower_bound = 1 
        upper_bound = n 

        while lower_bound <= upper_bound:
            our_guess = (lower_bound + upper_bound) //2

            check_guess = guess(our_guess)

            #Our guess is higher
            if check_guess == 1:
                lower_bound = our_guess + 1 
                 
            #Our guess is lower
            elif check_guess == -1:
                upper_bound = our_guess - 1

            else:
                return our_guess
        