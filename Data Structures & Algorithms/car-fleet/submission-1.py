

"""
target = 10 
position array [1,4] 
speed array    [3,2] 

iteration 0 : pos [1,speed = 3] , pos [4,speed =2] 
iteration 1 : pos [1+3 = 4, speed = 3], pos [4+ 2= 6,speed = 2] 
iteration 2 : pos [4+ 3 = 7, speed = 3], pos [6+2= 8,speed = 2] 
iteration 3 : pos [7+ 3 = 10, speed = 3], pos [8 + 2 = 10,speed = 2]


iterate until we reach the target 



6, 3, 1,8
8, 5, 2, 9
10, 7, 3, 10   1
10, 9, 4, 10


TIME TO GET THE DESTINATION IS IMPORTANT, that is the indicator that shows us that they collide.

if cars at lower positions have a lower time then one that has higher position, then we know they are quicker! 
"""
class Solution:
# target - position = distance until target 
#TIME = target - position / velocity  
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Python has this really cool built in keyword called zip that can combine two different
        # elements inside tuples, lists/arrays or strings into an array of arrays or dictionary
        pair = list(zip(position, speed))
        # We will sort but in the reverse order meaning the cars in the highest position will be first
        pair.sort(reverse=True)
        # We will then create a stack that will have the values OF TIME. 
        stack = []
        
        #NOTE: there is no enumerate, so we are iterating 
        # through pair where position and and speed are actual values in each pair!!! Enumerate uses indexes and values


        for position, speed in pair: 

            # Time calculation
            time = (target - position)/ speed
            # we will then append the time, and compare the times
            stack.append(time)

            # as long as we have greater then 2 values in our stack and if our last positions' time 
            #is less than the an earlier positions' time, we now there is a fleet of more than one car.
            #so we pop 
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        # The length of the stack gives me the  
        return len(stack)


            
            
        