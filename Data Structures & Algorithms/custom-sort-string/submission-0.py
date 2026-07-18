from collections import Counter

class Solution:
    """
    It is basically saying it wants us to order the given s string into the 
    same order given by the order string
    
    """
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)

        # NOTE: to append to a string we need to first make it a regular array 
        # Then we can use the method .join to make it back into
        # a regular string 
        returning_string = [] 

        for letter in order: 
            if letter in count:
                # THIS IS A CLEVER WAY TO APPEND instead of having to for loop it 
                # which would be more inefficient
                returning_string.append(letter * count[letter])

                # lastly we need to delete it, since we don't wanna use it anymore 
                # and so that we can append the remaining characters 
                # into our returning string 
                del count[letter]
        
        # We may have some random characters left that need to be appended 
        if count:
            # so we add the remaining left 
            for letter, frequency in count.items():
                returning_string.append(letter* frequency)

        # Lastly we join the array into a unified string using the .join method!
        return "".join(returning_string)
        

            


        