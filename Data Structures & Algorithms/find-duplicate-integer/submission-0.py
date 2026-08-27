# HashMap Solution
from collections import Counter
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # There is one exactly repeated integer, right of the bat im thinking hashmap
        count_int_hashmap = Counter(nums)


        for num in count_int_hashmap: 
            if count_int_hashmap[num] > 1: 
                return num
    
        return -1



        