
class Solution:
    def firstUniqChar(self, s: str) -> int:

        """
            n -> e,e,t,c,o,d,e,i,s,l,o,v,e 
            if it didn't find another that is equal to it in the string s 
            then we can go ahead and return that value, else we continue 

            to the next for loop and check e 
            n n
        """
        for index_outer in range(len(s)):
            no_duplicate = True
            for index_inner in range(len(s)):

                # If we are on the same index, we can't compare the same value so we just continue over the loop
                # The reason our range includes the complete len(s) for both for loops is cause if we hadb
                # a string n,n,e the second must check that the ones behind are repetitive too
                if index_outer == index_inner:
                    continue

                # If we find that the character is repeating, then there is no need to keep iterating in the inner loop
                # So in other words, we can check the next characters in string s , by breaking and to signal that we 
                #Encountered a duplicate, we can signal it false, and so we have to continue through our outer loop
                if s[index_outer] == s[index_inner]:
                    no_duplicate = False 
                    break

            #again by breaking out the outer loop, it's like we restart our check but with another character, and our no_duplicate assumption remains True until proven otherwise and if not we 
            #check for no_duplicate boolean
            if no_duplicate is True:
                return index_outer

        #return -1 by default if nothing appers 
        return -1

        