class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #By sorting we can easily and sequentially group the duplicates in order 
        #and "remove" duplicates quicker if they are next to eachother
        nums.sort()

        # result value being returned is a list of lists
        result = []
        



        # remember enumerate allows for position and value to be passed
        for position, value in enumerate(nums):

            # conditiob saying if we arent in the first position in the array, and

            # if the position we are in doesn't replicate the previous position then we continue to the next iteration of the loop

            # Example if we are on arr[2] in [-3,-3,1,2,4], at the point in -3, we would just continue over
            if position > 0 and value == nums[position - 1]:
                continue

            #left pointer should be the next one after position, think of position as our third pointerish 
            left_pointer = position + 1

            #right_pointer, always will be the last position in the array 
            right_pointer =len(nums) - 1 

            while left_pointer < right_pointer:
                threeSum = nums[left_pointer] + nums[right_pointer] + nums[position]
                
                if threeSum == 0 :
                    arr_combo = [nums[position], nums[left_pointer], nums[right_pointer]]
                    result.append(arr_combo)
                    left_pointer += 1
                    # Another check so that our left doesn't also account for duplicates, in this case
                    # we updates the value of our left pointer. Make sure we keep into account not going out of bounds 
                    while nums[left_pointer] == nums[left_pointer -1] and left_pointer < right_pointer:
                        left_pointer += 1  

                elif threeSum < 0 :
                    left_pointer += 1
                
                else:
                    right_pointer -= 1
            
        return result

            
                    





            

        


        