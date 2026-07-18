class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Brute Force solution: 
        Would be to check for duplicates, using a boolean variable,
        the variable would be True but turn false and exit out of the nested for loop
        if it finds an integer that doesn't have a duplicate 
        
        # O(n^2) Time complexity, and Space complexity is just O(1)
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
        """

        # ANOTHER way to approach this is by using hashset 
        # NOTE: the idea of a hashset or even the name itself!
        # the reason why that's better than using a "stack" is cause of the 
        # direct accessing of it by just simply uysing the keyword in, which checks for the key in teh hash set 
        seen_set = set() 

        # We loop through nums 
        for num in nums: 
            # if we have it already in our set we can remove it, we remove it to distinct the one's that appear twice with the one that appears once
            # if we add and remove, that's two moves hence those that are seen twice will be removed from the set.
            # The one that appears once will only be added and be the only one left in the set  
            if num in seen_set:
                seen_set.remove(num)
            else: 
                seen_set.add(num)
        return list(seen_set)[0] # Note sets can be referenced by index, hence we converted into a list to retrieve it   


        
        
    
            

        