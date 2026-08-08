class Solution:
    def climbStairs(self, n: int) -> int:
        # Brute force solution using the fibonacci idea

        """
        Basically same idea as the double branch fibonacci sequence, 
        except we need to change the base case idea, we need to return 1 
        (for valid step) if we have reached a clean 0, else we return a 0 if
        it wasn't a clean step ( We may have overshot by a step, making it 
        invalid)
        
        """
        """
        Now what if we bring it up a notch and now instead store it in cache using  
        memoization??
        
        """
        memoization_dict = {} 
        def dfs(current_step): 
            
            if current_step == 0:
                return 1
            elif current_step < 0:
                return 0
            if current_step in memoization_dict: 
                return memoization_dict[current_step]

            memoization_dict[current_step] = dfs(current_step-1) + dfs(current_step -2)  
            return memoization_dict[current_step]
        return dfs(n)
       
        
        