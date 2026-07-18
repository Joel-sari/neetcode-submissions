"""
What are we evaluating here? 

we are evaluating the sum of two digits squared!
Example: 
1^2 + 9^2 = 82


What makes a number happy?

A happy number is one that gives a sum of sqaures equal to 1 


lets say we are given 19

1^2 + 9^2 = 82 -> this is not a happy number, HOWEVER, the algorithm doesn't stop yet 
we take the answer we got and use that again to evaluate for happiness

now how long do we do this for? well if you actually work through the algorithm you'll notice that 
a cycle occurs in this algorithm/check. So we can use that as our stopping point for our algorithm 

NOTE: the problem mentions going infinitely (but obviously in code, we cna't have that happen)
so yeah the statment above explains how exactly we will solve this.


"""

class Solution:
    def isHappy(self, n: int) -> bool:

        
        
        # we will use this set to keep track of already calculated sum of sqaures
        #using this hashset, we are able to determine whether it's already been calculated in O(1) time
        visited_sum_of_sqaures = set()
        visited_sum_of_sqaures_result = n

        while visited_sum_of_sqaures_result not in visited_sum_of_sqaures:
            # if it isn't visited we can add it to our hashset immediately
            visited_sum_of_sqaures.add(visited_sum_of_sqaures_result)

            # we are adding a helper function to remove the clunkisness from our code!
            visited_sum_of_sqaures_result = self.sumOfSquares(visited_sum_of_sqaures_result)

            # base case/ ending point that determines happiness and we can return True and end the while loop
            if visited_sum_of_sqaures_result == 1:
                return True
        # just return false if we never reach happy number
        return False 

        
    def sumOfSquares(self, n: int):
        current_sum_of_sqaures = 0
        while n != 0:
            single_digit = n % 10 
            squared_single_digit_value = single_digit ** 2
            current_sum_of_sqaures += squared_single_digit_value
            n = n//10 
        return current_sum_of_sqaures



        

            



        