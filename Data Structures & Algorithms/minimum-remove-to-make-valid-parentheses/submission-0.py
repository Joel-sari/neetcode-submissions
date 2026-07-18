"""
This technique uses the ability of two passes in which we first filter out extra closing parenthesis and then extra opening parenthesis 

these two passes use two different arrays to append the filtered out parentehsis

"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # here we will append the characters we are going to keep and return from s 
        filtred_closing_parenthesis = []
        count = 0 # This count will keep track of whenever we come across an ooen parenthesis by +1 and when we reach a closed one we siubtract from the count 

        # We will skip some parenthesis for our putput
        """
        There are four different cases!
        
        
        """
        for character in s:
            if character == '(':
                filtred_closing_parenthesis.append(character)
                count+=1 

            # NOTE WE ARE CHECKING TO SEE IF WE ARE at a negative count (aka more closing parenthesis then opening ones!). If we aren't we can append it and lower our count  
            elif character == ')' and count > 0:
                filtred_closing_parenthesis.append(character)
                count -=1   

            # Why another elif instead of else? well cause there could be a chance the character could a ')' but our count is -1, we dont want to append that trash parenthesis AKA: closing parenthesis
            elif character != ')':
                filtred_closing_parenthesis.append(character)
            

            # Now we have filtered out the extra closing parenthesis! we still need to filter out the possible opening parenthesis!

        # NOTE AFTER APPLYING THIS FOR LOOP the fully filtered array will be in reverse order!
        filtered_open_parenthesis = []
        for character in filtred_closing_parenthesis[::-1]:
            if character == "(" and count > 0:
                count -= 1
            else:
                filtered_open_parenthesis.append(character)


            # So we can reverse the loop again just to ensure the strings we return is correctly returned 
            # Using the .join method makes the array a full string 
        fully_filtered_string = "".join(filtered_open_parenthesis[::-1])

        return fully_filtered_string
            

            


            

        