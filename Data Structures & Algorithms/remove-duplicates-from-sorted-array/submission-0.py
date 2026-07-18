class Solution:
    """
    The easiest and most obvious solution would just be to convert the array into a set and append those values back into a new array. 
    This uses O(n) space 
    still O(n) time complecity 

    and then on top of that we would still need to sort our array becasue sets aren;t sorted by the way they are added 
    
    
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        left_pointer, right_pointer = 0, 1 

        while right_pointer < len(nums):
            
            if nums[right_pointer] != nums[right_pointer-1]:
                left_pointer += 1
                nums[left_pointer] = nums[right_pointer]

            right_pointer += 1
        return left_pointer + 1
        
                

        

        




        

        