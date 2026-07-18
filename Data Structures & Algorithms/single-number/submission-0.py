class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Brute Force solution: 
        Would be to check for duplicates, using a boolean variable,
        the variable would be True but turn false and exit out of the nested for loop
        if it finds an integer that doesn't have a duplicate 
        """

        for i in range(len(nums)):
            duplicate = False
            for j in range(len(nums)):
                if i == j:
                    continue 
                if nums[i] == nums[j]:
                    duplicate = True 
                    break 
                    
            if duplicate is False:
                return nums[i]
    
            

        