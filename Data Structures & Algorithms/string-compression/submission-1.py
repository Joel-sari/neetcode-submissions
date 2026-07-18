class Solution:
    """
    The way we are kinda approaching this is having two pointers
    one pointer that follows (slacks back) and the other than keeps going until finding a new character

    
    """
    def compress(self, chars: List[str]) -> int:

        chars_length = len(chars)
        reader_pointer = 0
        writer_pointer = 0
        
      

        # if they chars length is either 1 0 then we know we will only have 1 in our s string
        if chars_length < 2: 
            return chars_length 
 
        while reader_pointer < chars_length : 

            # Count will need to reset each time we reach a new letter
            count = 1
            while reader_pointer < chars_length - 1 and chars[reader_pointer] == chars[reader_pointer + 1]  :
                count += 1 
                reader_pointer += 1

            

            #Once we reach a new character, we have a count that needs to be translated and written into the string 

            # FIRST WE NEED TO ENSURE THAT OUR CHAR[WRITER_POINTERS] Get overwritten correctly with the "new" character we are on!
            # EX: if we have a chars array  a a a b b b c c c, our chars[reader_pointer] will hold b which is neccessary to over write the a on the current chars! 
            chars[writer_pointer] = chars[reader_pointer]
            writer_pointer +=1 
            if count > 1:
                for char in str(count): # Note: str(count) makes it a string so that in the case count is multiple digits, it is seperated into seperate characters 
                    chars[writer_pointer] = char # By having the plus 1 we ensure writer_pointer 
                    writer_pointer += 1

            reader_pointer += 1

        return writer_pointer 
                


                
        
        
        
             

                
        
















"""
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


"""