class Solution:
    """
    The way we are kinda approaching this is having two pointers
    one pointer that follows (slacks back) and the other than keeps going until finding a new character

    
    """
    def compress(self, chars: List[str]) -> int:
        # first we need to specify the length of the List 
        num_of_char = len(chars)

        # Our base case which returns the same string if it's less than 2 aka 1 or 0 
        if num_of_char < 2: 
            return num_of_char 
        
        # these will be our pointers
        first_p, second_p = 0, 0

        # while we are still under the length of chars
        while first_p < num_of_char:
            count = 1

            # We make sure that we update the first_p
            while first_p < num_of_char - 1 and chars[first_p] == chars[first_p+1]:
                count += 1
                first_p += 1


            # We make sure that the last value of consecutive ones are updates at the second_p index in chars
            chars[second_p] = chars[first_p]
            second_p += 1  # we can then go ahead and update the second_pointer to the next place
            # remember in this next place we will update it with a numerical value 

            if count > 1: 
                # we are basically converting the count (if for example there is a two digit it becomes an array of 2 characters
                for value in str(count):
                    chars[second_p] = value
                    second_p += 1

            first_p += 1

        return second_p

             

                
        