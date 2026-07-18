class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        """

        Brute force solution!

        for outer_index in range(len(nums)-1):
            for inner_index in range(outer_index + 1, len(nums)):
                if nums[inner_index] == nums[outer_index] and abs(outer_index - inner_index) <= k:
                    return True 
        return False

        """
        # Lets use the sliding window technique! this would make the run time O(n) but space complexity is O(k)

        # first thing we need to do is keep track of our hashset 
        window = set()

        # again the hash set is so that  we keep track of the numbers added to our hashset already!
        left_p = 0 # start of ou window 
        for right_p in range(len(nums)):

            # OUR FIRST CHECK SHOULD CHECK FOR THE WINDOW SIZE!!!!! it must be less than or equal to k for us to return true  else we can just continue 
            if right_p - left_p > k: 
                # Now we need to update our window / left_pointer and remove the value from our set why?
                # well think about it, we wont take it into account anymore because our window has shifted 
                # and because it doesn;t fit what we wanted which was our window size to be less than k 
                window.remove(nums[left_p])
                left_p += 1 



            # if we have already come across the value!
            if nums[right_p] in window:
                # Then taht means we just found a dupluicate 
                return True
            window.add(nums[right_p])

        return False
             


        