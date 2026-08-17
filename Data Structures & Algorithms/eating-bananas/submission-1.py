"""
The problem: 

koko needs to eat tge bananas in the array
piles[i] = number of bannas in a pile 
i (each index) is a pile 
n amount of piles (length of the array)
h is the hours koko has to eat all the piles 


we are meant to return the smallest amount of hours per pile that barely satisfies the hours restraint given to us


the way we solve it is using a variation of binary search that doesn't use an array, rather uses the idea of a range.

"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # first lets define our range boundaries
        left_boundary, right_boundary = 1, max(piles)

        # by default the initial minumin of bph (bannas per hour) should be the right most value 
        minimum_bananas_per_hour = right_boundary

        while left_boundary <= right_boundary: 
            # this is our educated guess
            guess_of_hours_per_pile = (left_boundary + right_boundary) // 2

            hours_taken_to_eat_bananas = 0

            # now we must iterate throught the array piles, and determine the total of hours we take up using our guess of bph
            for banana_pile in piles: 
                # bananas /  (bananas /hours ) = bananas canceling each other out to give us hours
                hours_taken_to_eat_bananas += math.ceil(banana_pile/guess_of_hours_per_pile)

            
            # Here is where our condition / binary search logic occurs 

            # if we are less than the max hours, then we should STILL try to push amd see if we can get a smaller bph, we can do this by updating our right_boundary to be lower (trying a smaller guess)
            if hours_taken_to_eat_bananas <= h:
                minimum_bananas_per_hour = min(minimum_bananas_per_hour, guess_of_hours_per_pile)
                right_boundary = guess_of_hours_per_pile - 1

            # else we need a higher guess as the bph we came up with is too low to fit the hours given restrictioin
            else:
                left_boundary = guess_of_hours_per_pile + 1
            
        return minimum_bananas_per_hour
                

        