"""
There is always gonna be an integer before the bracket

how would we decode nested brackets???

3[a2[c]]

The 3 wants to multiply everything by 3 
and 2 wants to multiply the c by 2

NOTE: this is somewgat recursive!!

The nested bracket is a lil harder 

To solve the outer problem we need to solve the most bottom problem 


The closing bracket is where we are doing something different!

stack= 5,4,[,a,b,6,[, c,d,]
                         ^
                    at this point we stop appending to our stack!, we pop until opening bracket!
stack = 5,4,[,a,b,6,
                   ^
while isDigit for (cause there could be multiple remember!) , we pop and take the digits 
multiply it by the string inside the brackets and add those vakues into our stack 
stack= [5,4,[,a,b,6,cd,cd,cd,cd,cd,cd ]


stack= 5,4,[ <-- we pop until beginning bracket
And now we reached the end bracket, so we do the same process!!
so now we do the same thing and evrything that was popped previously is 
multiplied by the 54! 




"""

class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        for character in range(len(s)):
            if s[character] != "]":
                stack.append(s[character]) 
            else:
                sub_string_inside_bracket = ""

                # NOTE we are checking the top most value in the stack and seeing if it a opening bracket 
                # while it doesn't we can pop like normally 
                while stack[-1] != "[":
                    # NOTE THIS IS CRITICAL! we wanna add each character to the top of our substring 
                    # HOW IS THIS possible? WELL THINK BRO , concatenation!! not just doing += since 
                    # that would give us a wrong order
                    sub_string_inside_bracket = stack.pop() + sub_string_inside_bracket
                # We do also wanna POP THE OPEN BRACKET too "["
                stack.pop()

                # NOW WE WANNA PRESERVE THE K VALUE, how?? Well remember there is a chance we have 
                # more than one digit, so we must use a while loop as well !
                # NOTE, the stack can reach out of bounds so here we do need to check we ae in bounds 
                #
                #k is the number being multiplied!
                k = ""
                while stack and stack[-1].isdigit(): 
                    k = stack.pop() + k

                stack.append(int(k)* sub_string_inside_bracket) 
        return "".join(stack)



                

            


        