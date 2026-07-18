"""
Distinct integers candidates and a target integer are given. 

We want to return a list of all unique combinations of candidates where the
chosen numbers sum to target.

they may be returned in any order

We don't want the same combinations! 

combinations not permutations!! 

ex: 

3,2,2 = 7

2,2,3 = 7 NOte: SAME combination, which is NOT WHAT WE WANT

EX: 

2 3 6 7 

"""

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        #index keeps track of the pointer to the left of the array,
        # current keeps track of what values we had added so far to our current combination
        # and total is the sum of the combination
        def dfs(index, current_combo, total):
            #Our base case, is if we found a target combination
            if total == target:
                #We want to create a copy because we want to use this combination of variables for another 
                #combination calculation in our recurisve algorithm, prevents modifications!
                result.append(current_combo.copy())
                return 
            # if we get out bounds we should BOUNCE out of the recursion
            # or if our combinations become bigger than our target then there 
            # is no point in continuing our search
            if total > target or index >= len(nums):
                return

            # Now for our actual recursive step, 
            #we can choose to include the value of candidates at index
            current_combo.append(nums[index])
            #now we are going to recursively call dfs 
            #REALLY IMPOTANT NOTE:
            #When recursively going through this algorithm using the 2 3 6 7 , target = 7 example
            #AT THE END OF THE RECURSION for 2 we reach [2,2,2,2] with total = 8 
            # because 8 > 7 we know to end it HOWEVER NOTICE: WE ALREADY APPENDED TO OUR COMBO
            #meaning current_combo = [2,2,2,2] and STAYS THAT WAY even if go back from dfs(0, [2,2,2,2], 8) to dfs(0, [2,2,2,2], 8)
            # BECAUSE WE APPENDED TO THE LIST!! and it translates over! TARGET THO CHANGES BACK TO 6 
            # Thus, giving us the reason to having to pop current combo before going to our second decision!
            dfs(index, current_combo, total + nums[index])
            current_combo.pop()
            dfs(index + 1, current_combo, total)
        

        dfs(0, [], 0)
        return result
    




        