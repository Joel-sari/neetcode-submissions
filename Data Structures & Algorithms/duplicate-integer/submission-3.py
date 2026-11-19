class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict_counter = {} 
        for num in nums: 
            dict_counter[num] = dict_counter.get(num, 0) + 1
            if dict_counter[num] > 1: 
                return True 

        return False

        
        