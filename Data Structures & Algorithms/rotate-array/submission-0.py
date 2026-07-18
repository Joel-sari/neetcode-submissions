class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        the simple way is just using another array and using OUR MODULUS by length of the array/string 


        
        # My first intuition idea, thus uses O(n) space and O(n) time complexity 
        # where I plan on using k + index % modulus len(nums)to map out the placement of the 
        # array elelemnts, we will have too apply it to a new array 

        # we need to create this temporarry array with dummy values as we will be overriding them by mapping out to the correct index
        temporary_array = [0] * len(nums)

        for num_index in range(len(nums)):
            shifted_index = (k + num_index) % len(nums)
            temporary_array[shifted_index] = nums[num_index]
        
        nums[:] = temporary_array


        # But now can we do this without using extra space??

        """

        # Yes we can! how? well it's not intuitive at all but by reversing the array, and then
        # reversing again based on the k values we get what we want, take a look at an example:

        """
        [1,2,3,4,5]  and k = 2

        thus we can reverse it 

        [5,4,3,2,1] but then look! from 0 :k if we reverse we get: 

        [4,5, 3,2,1] then we cam just reverse from 2 to len(nums) -1

        and we modify the array in place!

        NOTE by reverse, we don't mean reverse in a sorted form so be VERY CAREFUL!
        """

        # NOTE EDGE CASE, k could be larger than the length of nums, but rememeber 
        # a rotation of 1 is the same as a rotation of 4 in a len(nums) = 3 
        k = k % len (nums)

        # NOTE this is the FIRST Reversing, and note, since we will be reversing a lot, why don' we just make it 
        # afunction??
        # We will be reversing by using left pointer!, we just swap left and right_pointer 
        


        def reverseElements(left_p, right_p):
            # basically just swapping until both poointers meet
            while left_p < right_p:
                nums[left_p], nums[right_p] = nums[right_p], nums[left_p]
                left_p += 1
                right_p -= 1

        # FIRST WE REVERSE THE WHOLE ARRAY 
        reverseElements(0, len(nums)-1)

        # Next we reverse again based on the k value which indicates the the stop to the righ rotated stuff at the beginning of the array 
        reverseElements(0,k-1)
        # Then we rotate the rest by going from k all the way to the end of the array
        reverseElements(k,len(nums)-1 )


        



        
            

        