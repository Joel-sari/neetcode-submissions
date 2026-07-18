class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        """
        O(n^2 solution)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    target_pair = [i, j]
                    return target_pair
                
        return []
        """
        """
        # THIS IS ASSUMING YOU CAN SORT

        nums.sort() # O(nlogn)

        left_pointer = 0 
        right_pointer = len(nums) - 1

        while left_pointer < right_pointer:

            sum_of_pointers = nums[left_pointer] + nums[right_pointer]

            if sum_of_pointers == target: 
                return [left_pointer, right_pointer]

            elif target < sum_of_pointers: 
                right_pointer -= 1
            else: 
                left_pointer +=1 


        return []
        """

        hash_value_to_index = {}

        #this is the one pass method!
        for index_value, num_key in enumerate(nums):
            difference = target - num_key 
            if difference in hash_value_to_index: 
                target_pair = [hash_value_to_index[difference], index_value]
                return target_pair
            
            hash_value_to_index[num_key] = index_value


            

        
        
            

        


        