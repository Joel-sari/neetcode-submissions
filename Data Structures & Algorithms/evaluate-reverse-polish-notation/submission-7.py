"""
1,2, + ->> 1+ 2

1, 2, + 3, 4, *  ->> 1 + 2


the o


"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else: 
                b = stack.pop()
                a = stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    #Notice that a/b itself instantly rounds to 0,
                    #so the only thing left to do is wrap it by the int keyword to make sure 
                    #tha value returned is an int. 
                    stack.append(int(a/b))
        return stack[0]


                
                
            

            
                

            



        