"""
Given a target arrau we want to form 

Example 
target = 1,2,3,2,1
initial = 0,0,0,0,0

only operation to make initial become target is selecting a subarray and then incrementing every value in the subarray by 1

we want to return the minimun number of operations (minimum amount of subarray additons created)

greedy solution!

be simple and efficient. 


Algorithm: 

(Before we dive in: Think of this problem as having hills, if there is one big hill (ex 1,2,3,2,1) then they all share operationss but if there are multiple disconnected hills, that could lead to more operations (ex 1,2,3,2,1,1,2,3,2,1))

1. - create a number of operations integer ( set it to the first element in the array) that scans through the array and adds to the number of operations based on the values it comes through the target array 

    1.2 if the current target[i] is bigger than target[i -1 ] then: 
            number_of_operations +=  target[i] - [i -1 ] ( the jump difference between the two )
    1.3 if the current target[i] is less than or equal target[i -1], we dont add to our number of operations 


why this works? 

basically because of the contiguous property, we can just detect whether there is another hill by checking neighbouring index values, if there is a sign of an increase (another hill) then we need to add to our operations, else we can keep it the same 

 also the fact that we can only add up by 1 helps us a lot too. lasyly


"""
class Solution:
    def minNumberOperations(self, target: List[int]) -> int:

        

        if not len(target):
            return 0 
        
        number_of_operations = target[0]

        for index in range(1, len(target)):
            if target[index] > target[index - 1]: 
                number_of_operations += target[index] - target[index - 1]
        
        return number_of_operations

            
        