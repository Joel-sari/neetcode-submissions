class Solution:
    """
    temperatures[i] represents the daily temperatures on the ith day 
    
    we need to retun a result array where result[i] = NUMBER OF DAYS AFTER the ith day before a warmer temp appears on a future day 
    
    """

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        """"
        Brute Force Solution: 

        # this will be the array that we return
        result = []

        # we are looping through each index in the temperatures array 
        for index in range(len(temperatures)):
           
            # We can already start our next_index to the next one since we are going to compare with the next element
            next_index = index + 1

            # we can safely say its 1 for now as we will do a double check later to ensure that if we 
            #can't find a day with a lower temp, we can set it to 0
            count = 1

            # we check while we are in bound, we can increase next_index, we the b reak out if our next_index value is greater (menaing we found it!)
            while next_index < len(temperatures):
                if temperatures[next_index] > temperatures[index]:
                    break 
                # if we dont find it we can keep searcjing through the array using next_index and we will increase count+=1
                count +=1
                next_index+=1

            if next_index == len(temperatures):
                count = 0 

            # Append our count to our array 
            result.append(count)
        return result 
        """

        #THIS SOLUTION IS SO GENIUS!!!, it uses O(n) space but.....
        # its time complexity is O(n) cause of the simeltaneous changing of arrays, we do this by storing both the index and the value ityself 
        result = [0] * len(temperatures)

        #We need a second array to be the stack, again this stack will hold both the index value and the actual temp value 
        temperatures_and_index = []

        # Now we need to loop though the given array, we willa lso need a while loop in the case we come across values/temp that
        # are less than the previous days temp, LETS USE ENUMERATE!! NOTE : It's important to keep track of the index 
        #To use for our calculations
        for index, temp in enumerate(temperatures):


            # While the temperature in enumarate is less than the greatest temp we have at the endof  our stack!

            # REMEMBER Stack[-1] refers to the last element in the stack, andthe [0] is the first element in that specifc element array
            #Also note stack will intially be empty and can be empty towards the end!!!
            # ALSO NOTE: That while and pop will take care of each comparison being different from the previous!
            while temperatures_and_index and temp > temperatures_and_index[-1][0]:
                #  We need to retrieve the index value, because we need to retrive an array element, we need both it's values 
                stack_temp, stack_index = temperatures_and_index.pop()
                result[stack_index] = index - stack_index
            temperatures_and_index.append((temp, index))
        return result






     
    
    

    
        