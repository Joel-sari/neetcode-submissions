# Solution with dictionary
from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # default dict is good to use so that we dont have to check for an empty array
        hashmap = defaultdict(int)

        for index, num in enumerate(nums): 
            if (target - num) in hashmap:
                return [hashmap[target - num], index]
            hashmap[num] = index

        