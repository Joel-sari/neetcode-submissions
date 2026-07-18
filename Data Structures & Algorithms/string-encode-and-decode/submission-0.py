"""
    but what if the special character is in the GIVEN WORDS, so now 
    let's think, maybe if we keep track of the number of characters that could 
    be another way

    Notice the problem doesn't allow for extra data strcuture space, knowing this
    we need to note that we might have to add it to the exsiting string given

    we will put this number values in the beginning, we will use a delimeter
    the pound sign

    EX)

    4#neet5#cod#e
"""

class Solution:

    # Note: ANY CAHARCTER can be used

    

    #Encode into a single string, given a list of strings
    def encode(self, strs: List[str]) -> str:


    #When combining different words, if we naively just combined them,
    #theres no way to keep track when we need to decode, we need to use a 
    #special character to seperate it 

    
        result = "" # single string


        # This is how we are putting all of it together in one string
        for s in strs:
            result += str(len(s)) + "#" + s
        return result
        

    #This takes a single sting and braks it up in an array     
    def decode(self, s: str) -> List[str]:
        result, index = [], 0

        # still in bounds
        while index < len(s):
            j = index

            #character at pointer j doesnt equal 
            #keep incrementing till we get to the pound character

            while s[j] != "#": # this is getting the number, (It's a while loop in case it bigger than 1 digit yk)
            #Again we increment by charcetr and stop on the FIRST #
                j += 1
            
            #We then take the beginning index from start to where j ended up staying for the #
            # meaning the length of the string in the begginning and convert it into an integer
            length = int(s[index : j]) 

            # this length character tells how long our string will be to split into an array of strings

            # So now we have our pointers! j + 1 starts after the # value and length is the length of the string we need to read/write
            # by using str[splicing:], we are able to list the range we want!
            result.append(s[j + 1: j + 1 + length])
            index = j + 1 + length
        
        return result

