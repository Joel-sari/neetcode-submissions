"""
This is a DP programming problem!
"""

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        total_string = s
        
        # Right now we are defining a cache that lays out an array of Booleane variables!
        dynamicprogramming_CACHE = [False] * (len(s) + 1)

        dynamicprogramming_CACHE[len(s)] = True 

        # Why + 1 , well the last one is our base case, meaning it will hold the True boolean variable 
        # Think about it like this is the one where we reach the end/ successful state of the DP alogotihm

        for index in range(len(s)-1, -1, -1):
            for word in wordDict: 
                # Our first comparison here is to determine if
                # our current word (think of it like substringish)
                # is in bounds , remember index starts high in the string 
                if (index + len(word)) <= len(total_string) and s[index: index + len(word)] == word:
                    
                    # Using our base case to set the word found to true in our DP CACHE Boolean Values
                    dynamicprogramming_CACHE[index] = dynamicprogramming_CACHE[index + len(word)]
                # As soon as we get one word that we can word break, we can breka out of the inner loop

                if dynamicprogramming_CACHE[index] is True:
                    break
                    
        # if it worked for the whole total string then DP CACHE 0 position should hold the TRUE value and 
        # that reflects whether the WHOLE Total string was succesful
        return dynamicprogramming_CACHE[0]



        

        

        