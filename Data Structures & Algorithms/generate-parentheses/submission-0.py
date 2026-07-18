class Solution:
    # n defines the amount of pairs of parenthesis (pair = open and closed parenthesis)
    """
    To approach the problem, lets go over all the edge cases 
    1. notice you can NEVER start with a close parenthesis
    2. Lets have a count of open parenthesis and closed parenthesis
    Lets run through an example 
    n = 3 
    open = 3
    close = 3


    case 1: [ () ]
    open = 3 -> 2 
    closed = 3 -> 2


    case 2: [ (( ]
    open = 3 -> 2 -> 1 
    closed = 3 


    case 3 (cannot happen!):   [ ( )) ]
    open = 3 -> 2
    closed = 3 -> 2 -> 1




    what pattern are we noticing here?? 
    well looking closely at he counts, it unaccepatbel for the closed to be ever less than open!

    condition of adding a closing parenthesis, 
    can only add it if count_left ( if we started at 3) > open 
    ca


    
    
    """
    def generateParenthesis(self, n: int) -> List[str]:

        stack_temp_paranthesis_holder = []

        parenthesis_combinations = []

        def backtracking(open_count, closed_count):
            # remember n defines how many pairs are available!, this our base case, that says we are done!
            if open_count == closed_count == n:
                # REMEMBER .join takes in an array of strings 
                parenthesis_combinations.append("".join(stack_temp_paranthesis_holder))
                return
            if open_count < n:
                stack_temp_paranthesis_holder.append("(")
                backtracking(open_count + 1, closed_count)
                stack_temp_paranthesis_holder.pop()
            if closed_count < open_count:
                stack_temp_paranthesis_holder.append(")")
                backtracking(open_count, closed_count + 1)
                stack_temp_paranthesis_holder.pop()

        backtracking(0,0)
        return parenthesis_combinations
            





    


        