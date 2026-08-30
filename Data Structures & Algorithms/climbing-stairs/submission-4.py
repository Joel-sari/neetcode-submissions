from collections import defaultdict
class Solution:
    def climbStairs(self, n: int) -> int:

        cache_results = {0: 0, 1: 1, 2: 2}
        

        def dfs_fib(n): 
            if n in cache_results: 
                return cache_results[n]
            cache_results[n] = dfs_fib(n - 1) + dfs_fib(n - 2)
            return cache_results[n]
        
        return dfs_fib(n)
