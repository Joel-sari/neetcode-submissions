class Solution:
    """
        first thing to note is that our shift must be modded by the the length of our string 
        why?

        Well think about shifting by 1 when s has length of 6 and shifitng by 7 has the SAME EFFECT!
        Thus, removing the extra shifting not only makes it shift less but it makes the logci much easier for string slicing
    """
    """
                tip: the best way to visualize this is by using numerical values and the string 
                LEFT SHIFT:
                s n h j q w
                0 1 2 3 4 5

                if we shift by left by 2 we get 
                h j q w 
                2 3 4 5   

                which we can add with the rest by just doing [:2]  + s n

                THUS, [amount:] + [:amount]

                SHIFT RIGHT LOGIC:
                

                s n h j q w
                0 1 2 3 4 5

                if we shift by right by 2 we get 
                q w s n h j 
                4 5 0 1 2 3

                NOTE: 
                we want len(s) - amount to slice and use as our breaking point

                [len(s)-amount:] + [:len(s)-amount]
                
    """
    
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        
        # PLEASE NOTE: if there is a fixed amount of ints in a list of lists YOU CAN DO THIS FOLLOWING FOR LOOP: 
        for direction, amount in shift: # direction referes to shift[i][0] and amount refers to shift[i][1]
            amount %= len(s) # Ex if 7 = amount and len(s) = 6 so the shift would be 1 
            if direction == 0: 
                #left makes sense, the starting point would be the amount shifted all the way to the end 

                #0 = left direction thus
                s = s[amount:] + s[:amount]
            else:
                s = s[len(s)-amount:] + s[:len(s)-amount]
        return s 

        