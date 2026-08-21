"""
For this problem, utilize the backtracking algorithm. Moreover, remember the use of a decision tree 
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        list_of_subsets = []

        current_subset = []
        def backtracking(index):
            # base case is if the index is out of bounds or greater than nums 
            if index >= len(nums):
                list_of_subsets.append(current_subset.copy())
                return

            # Left branch, that includes nums[i]/the numeric value 
            current_subset.append(nums[index])
            # iterate/recursion through the other possibilities now
            backtracking(index + 1)

            # decision if you were not to take the number and just be empty
            # think of it as once we hop out the first recursive call this is how our subset list would look like : 
            """
            [[1,2,3]] -> Just added 

            [1,2] -> Now we are here, we popped 3 from our subset, and we still increase index which will ultimately still end our subset due to the base case.
            
            """
            current_subset.pop()
            backtracking(index + 1)
        backtracking(0)
        return list_of_subsets




            
            
            
        