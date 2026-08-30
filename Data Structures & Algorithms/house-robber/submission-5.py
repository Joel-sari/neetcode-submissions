from collections import defaultdict
class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = defaultdict(int)

        def dfs(index): 
            # we aren't
            if index >= len(nums): 
                return 0

            if index in cache: 
                return cache[index]

            result = max(dfs(index + 1), nums[index]+ dfs(index + 2) )
            cache[index] = result
            return result
    
        
        return dfs(0)
