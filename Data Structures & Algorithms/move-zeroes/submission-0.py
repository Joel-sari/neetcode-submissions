class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        [1,2,5,0,0,0]
             ^     ^

        [1, 2, 5, 0, 0, 0]
        
        """
        reader_p, writer_p = 0, 0 

        while reader_p < len(nums):
            if nums[reader_p] != 0:
                nums[reader_p], nums[writer_p] = nums[writer_p], nums[reader_p]
                writer_p += 1

            reader_p += 1

        


            
        
        