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
        triplet_combinations = set()
        

        for first_index in range(len(nums)):
            for second_index in range(first_index + 1, len(nums)):
                for third_index in range(second_index + 1, len(nums)):
                    if nums[first_index] + nums[second_index] + nums[third_index] == 0:
                        temp_tuple = tuple(sorted([nums[first_index], nums[second_index], nums[third_index]]))
                        triplet_combinations.add(temp_tuple)
        return [list(triplet_combo) for triplet_combo in triplet_combinations]



        