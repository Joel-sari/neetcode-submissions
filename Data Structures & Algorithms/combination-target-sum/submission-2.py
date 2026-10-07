class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        subset = []

        def dfs(i):
            if i >= len(nums) or sum(subset) > target: 
                return
            
            if sum(subset) == target:
                result.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i)

            subset.pop()
            dfs(i + 1)
        
        dfs(0)
        return result