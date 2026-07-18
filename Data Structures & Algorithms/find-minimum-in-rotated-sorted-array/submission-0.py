"""
The main idea is that we have a sorted array with "rotation"
which just means we our last elements go to the front and all the numbers shift per rotation


The easiest and most convenient way would just be to find the minumum in the array and return that but that would 
be O(n)

we will use binary search, but in a weird way 

we use pointers!! and a middle pointer!

the question to solve and logic behind this, we choose the middle position and
checking okay, is the middle position in the left side of the sorted array or right? 

Ex: 3 4 5 1 2 where 5 is the middle position, in this case it would be the left side of the array

well we dont want that we actually want to be on the rigth side as teh right side has teh samller values!

So the way we determine where we are in the right or left side is by comparing WITH THE BEGINNING 

saying if nums[median] >= nums[left_pointer] why? well remember!
the left side is gonna have the LARGER VALUES!, thus we wanna get away from it 

why greater than or equal? well because if our midpoint was at the beginning and left was at the begiining then poth 
pointers point at the same thing 

So BASICALLY if the pointer is on the left side of the array we want to move to the right and if 
we are on the right side, we want to move to the left (if there is NO DIP, meaing if it's consecutive)
        
"""
class Solution:
    def findMin(self, nums: List[int]) -> int:

        # settinga default minimum to any value
        minimum = nums[0]

        # setting left and right pointer to 0 and last pointer in the end 
        left_pointer, right_pointer = 0, len(nums) -1


        # While both pointers don't cross
        while left_pointer <= right_pointer:

            # if the first value in the array is less than the last why? this automatically tells us
            # that for a subarray, it alreadu is sorted thus we can just break out of the while loop
            if nums[left_pointer] < nums[right_pointer]:
                # again this crucial in breaking the loop
                minimum = min(minimum, nums[left_pointer])
                break
            
            # So them if it isn't sorted then we can continue on with the while loop
            # using the median value and storing it as our minimum if it is minimum
            median = (left_pointer + right_pointer) //2
            minimum = min(minimum, nums[median])

            #Now we need to know if we need to search to the left or right based on if the 
            #median is greater than or equal to the left_pointer, then we update the right or left pointers 
            if nums[median] >= nums[left_pointer]:
                # if the median is greater than the left beginning we can checl the right sub array
                left_pointer = median + 1         
            else: 
                right_pointer = median - 1


            """
            lets say we have 

                     
                              l  m  r
            4 , 5 , 6 , 7, 8, 1 , 2 , 3
            """
        return minimum
            



            

            





        
        