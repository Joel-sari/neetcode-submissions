"""
Remember that order does't matter for combinations thus 
2,1 is the same as 1,2

how do we make this possible? We do so by choosing values to be part of the combination that are greater than the current number you are in l



NOTES AFTER NEETCODE: 
WE ARE GONNA SOLVE THIS RECURSIVELY!
we will be using backtracking and decision tree! the time complexity will be k * n^k

"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        list_of_combos = []

        
        def backtrack(starting_value, current_combination):
            # What is the base case? Well remember we are gonna stop once we reach the length of k 
            if len(current_combination) == k:
                # we found a combo and we are gonna add to our list_of_combos!!
                list_of_combos.append(current_combination.copy())
                return 
            for number in range(starting_value , n + 1):
                current_combination.append(number)

                # now we are fonna recursively call index + 1 to go to the next one
                backtrack(number+1, current_combination)

                # Now we want to cleam up! what does this mean? We want to remove/clean up the combination array for the next iteration  
                current_combination.pop()

        backtrack(1, [])

        return list_of_combos
        
                    

         
        