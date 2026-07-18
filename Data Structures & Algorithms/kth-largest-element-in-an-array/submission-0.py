class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Obvious Answer with Time complexity of O(nlogn)

        nums.sort() 
        
        ex:
        [1,2,3,4,5]
         0,1,2,3,4,5

         5 - 1
         is 3
        
        return nums[len(nums) - k ]

        """
        
        # Can we do better?, we can use MIN HEAPS!
        """Why a min-heap is exactly what we want for “k largest”

            We don’t want a heap of all elements. We want a heap of size k that always contains the k largest seen so far.

            If we keep k largest, the “most useless” among them is the smallest of the k largest — that’s the one we want to kick out first when we find a bigger number.

            Yep — that’s pretty much it:
	    •	heapq is a min-heap
	    •	nlargest(k, nums) uses that min-heap as a tool to keep the k largest by constantly 
        kicking out the smallest among the kept items.

        In my own words: we basically use minheaps to sort out our initial min heap of size k 
        then compare its values /replace them with the largest values in the rest of the array 
        It lastly sorts the values in k in desceding order


        return heapq.nlargest(k, nums)[-1]
        """

        # Now for Quick select
        """
        NOTE: This algorithm is basically qucik sort but instead of sorting both sides
        meaning the less than pivot side and the greater than pivot size, we only go for one by comparing
        the k value with the index
        """

        target_index = len(nums) - k #NOTE: we although we know the position, the array still needs to be sorted!!

        def quickSelect(left_pointer, right_pointer):
            pivot = nums[right_pointer] # the array all the way to the right 
            pointer = left_pointer # the start of the "subarray" or subsection of the array 
            
            #We iterate through the whole sub array to do the swapping
            # we have a pointer that moves based on the comparison of pivot, it swaps with the index EACH TIME 
            # it is less than the pivot (pointer also increases after swapping), else our index increases but our pointer remains.
            for index in range(left_pointer, right_pointer):
                if nums[index] <= pivot: 
                    # swap occurs between the element at index and the element at pointer 
                    nums[pointer], nums[index] = nums[index], nums[pointer]
                    # We increase pointer by 1, as everything to the left is "organized "
                    pointer+= 1
            # Lastly we have reached the end/ our pivot, so we need to put the pivot in it's correct spot 
            nums[pointer], nums[right_pointer] =  nums[right_pointer], nums[pointer]


            # NOW WE NEED TO SEE WHAT RECURSIVE FUNCTION WE NEED TO DO!
            #how?
            #we need to compare pointer ( where are pivot is at) with the target index
            if pointer > target_index: 
                # NOTE: it is pointer - 1 because we aren't splicing! what we pass in is that actual "ending" point 
                # Also note that the pointer is sorted, thus we don't need to touch it whatsover
                return quickSelect(left_pointer, pointer - 1)
            elif pointer < target_index: 
                return quickSelect(pointer + 1, right_pointer)
            else:
                return nums[pointer]
        
        return quickSelect(0, len(nums) - 1)





        



        
        

        