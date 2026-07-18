class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        """
        So our intial thought process is to 1, have all the values we care about 
        AKA those in nums and it's index value to then later map the values we want correctly 
        into the array we are going to return (result array)

        """
        nums1_indexes = { num : index for index, num in enumerate(nums1)}

        # we intialize an array of size of the nums1 with -1 values as default 
        # so that if we don't find a next greater element the value remains -1 by default 
        greater_element_array = [-1] * len(nums1)

        for outer_index in range(len(nums2)):
        # We are checking to see if the current element in the array nums2 is even in nums1_indexes dictionary 
            if nums2[outer_index] not in nums1_indexes:
                # if it isn't then we know not to evaluate this and skip it, the continue keyword goes to the next iteration of the loop 
                continue  
            
            # So because we are checking only the elements after outer_index, then our range "decreases", in which we check to the right of our current value
            for inner_index in range(outer_index + 1, len(nums2)):
                if nums2[inner_index] > nums2[outer_index]:
                    
                    # This is the key of the dictionary that holds the index, key: index 
                    key_to_nums1_hash = nums2[outer_index]

                    # This gives the correct index value, where we need to adjust the index's value in greater_element_array
                    num1_index = nums1_indexes[key_to_nums1_hash]

                    # This holds the next greater elemebt so that we can cleanly change the value in the array
                    greater_element = nums2[inner_index]

                    greater_element_array[num1_index] = greater_element

                    # We are done with this inner loop, meaning we are done checking for next greater elments at this index
                    break

        return greater_element_array
                    



        