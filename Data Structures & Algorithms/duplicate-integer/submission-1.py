class Solution:
    def hasDuplicate(self, nums: List[int]):
        hashymap = {} 
        duplicate_status = False

        for pointer in range(len(nums)):
    
            if nums[pointer]  in hashymap:
                duplicate_status = True
                return duplicate_status

            hashymap[nums[pointer]]= pointer
            
        return duplicate_status
        


        