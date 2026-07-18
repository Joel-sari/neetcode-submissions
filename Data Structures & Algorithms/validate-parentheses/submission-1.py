class Solution:
    def isValid(self, s: str) -> bool:

        hashy = {")":"(", "}":"{", "]":"["}
        stacky = []

        for char in s:
            if char in hashy:
                # checking if stack isn't empty and checking the last value in the stack 
                # checking the last value in the stack is what makes sure that the parenthesis are in order!!!
                # This would not work for ({)} because the the stack would be [ (,{ ] and 
                # if we check stack [-1], it doesn't match it with the hashy[ } ] value
                if stacky and stacky[-1] == hashy[char]:
                    stacky.pop()
                else :
                    return False
            else:
                stacky.append(char)

    # if at the end the stack is emptyu, that means we've matched all parenthesis
        if not stacky:
            return True
        else: 
            return False
    
                

      




        