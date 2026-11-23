class Solution:
    def numDecodings(self, s: str) -> int:
        # our base case is just 1 for the length of the string = 0 
        dp_cache = { len(s): 1}

        # recursive function 
        def dfs(index): 
            # note we exit out once we reach the length of our string s 
            if index in dp_cache: 
                return dp_cache[index]

            # no way to decode out string 0!
            if s[index] == "0": 
                return 0 # invalid case
            
            result = dfs(index + 1)
            
            # if i + 1 is in bounds, and our current digit is 1! (all teens are acceptable )
            if (index + 1 < len(s) and (s[index] == "1"
                or 
                s[index] == "2" and s[index + 1] in "0123456")): 

                # note this adds the cached result 
                result += dfs(index + 2)

            dp_cache[index] = result 

            return result 

        return dfs(0)
                
        
        