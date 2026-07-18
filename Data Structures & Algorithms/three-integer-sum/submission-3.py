"""
NOTE: we cannot contain any triple duplicates!! 
What that essentially means is there should not be a chance in where
there are same combinations of triplets!!

how do we avoid this? 
there are multiple ways and we will use combinations of sets 
or checking adjacent values
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Brute Force solution
        """
        triplet_combinations = set()
        

        for first_index in range(len(nums)):
            for second_index in range(first_index + 1, len(nums)):
                for third_index in range(second_index + 1, len(nums)):
                    if nums[first_index] + nums[second_index] + nums[third_index] == 0:
                        temp_tuple = tuple(sorted([nums[first_index], nums[second_index], nums[third_index]]))
                        triplet_combinations.add(temp_tuple)
        return [list(triplet_combo) for triplet_combo in triplet_combinations]

        """

        unique_triplet_combinatons = []

        #NOw using pointers solution, this is more optimal!!

        # first we need to sort the array itself!!
        nums.sort() 

        for current_position, current_value in enumerate(nums):

            # We need to skip the current_position if we have a repeat in the last one! 
            if current_position > 0 and current_value == nums[current_position -1]: 
                # we skip the iteration 
                continue 

            # From here on out it's pretty much the Two Sum Algorithm!
            left_pointer = current_position + 1

            right_pointer = len(nums) - 1 

            while left_pointer < right_pointer:
                
                potential_triplet_3sum = current_value + nums[left_pointer] + nums[right_pointer]
                if potential_triplet_3sum == 0:
                    triplet_combo = [nums[current_position], nums[left_pointer], nums[right_pointer]]
                    unique_triplet_combinatons.append(triplet_combo)
                    left_pointer += 1 

                    # Why only in here? Cause only at this point do we care that we don't want duplicates!
                    # For EX: if we ran into another duplicate before but it wasnt a combo that added to 0, then who cares 
                    # cuase it's not added into our result array 
                    while nums[left_pointer] == nums[left_pointer - 1] and left_pointer < right_pointer:
                        left_pointer += 1
                elif potential_triplet_3sum < 0: 
                    left_pointer += 1
                else:
                    right_pointer -= 1
        return unique_triplet_combinatons
                
                    







        