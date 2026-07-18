"""
k = bananas per hour (ratio)
piles[i]= number of bananas in the pile at that index 
h = hours you have to eat all bananas 

using our k we will determine how many bannas per hour we can eat 

if the pile has less than k bananas, then u need to wait before nmvoing to another 

return the min integer k such that we can eat all bannas within 9 hours


Running through an example: 


piles [3,6,7,11]

# We know that the maximum k we can have that will fit would be highs pile of bananas of the array


We use the max of the pile to fill out a range of arrays

k = [1,2,3,4,5,6,7,8,9,10,11] 
we will have a left and right pointer , at the beggining and the right


NOTE: WE WILL ROUND UP!!!, listen so the algorithm for k is # number of bananas in the pile / divided by option k value 

WHY BINARY SEARCH?? WELL LETS RUN THROUGHT IT 

in our first iteration we land on 6, (possible k):

we then use that k to divide with our different piles and round up to get the hours 

piles [3,6,7,11]
3/6 = 1, 6/6= 1 7/6= 2, 11/6 = 2 Thus 1+1+2+2 = 6! This is less than 8 hours!! This is pretty good 
But remember WE WANT THE LOWEST AMOUNT OF K!!! Thus it is possible that we get a low k but an equal or "high" amount of hours (as long as it is less than h)


but now we must check for the MINIMUM, how do we do that? well since we are less than k we can search the LEFT SIDE 

If we went over the threshold? we go to the right!!!


So once again the problem is essentially looking for 

The lowest amount of bananas eaten in an hour (k) that falls between 0 and h hours 

"""


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        

        # Okay so again how this works is we are creating these two pointers for our "range" for the binary search! 
        # Note we aren't even actually using an array for this, just simply the range itself and division (which is invisble lowkey)

        left_pointer, right_pointer = 1, max(piles)

        # we know we can say that the base case starts with the max amount in the pile
        minimum_result_banana_per_hour = right_pointer 

        while left_pointer <= right_pointer:
            # remember the double divide by 2 is int floor division 
            bananas_per_hour_possibly = (left_pointer + right_pointer) // 2

            # Note now that we have pointed out our potential k value we must ensure it falls under the h}
            #given hours!
            total_hours_it_takes_to_eat_bananas = 0 
            for banana_pile in piles: 

                # think of like meters / m/s = s 
                total_hours_it_takes_to_eat_bananas += math.ceil(banana_pile/bananas_per_hour_possibly)

            # Remember we can only count 
            if total_hours_it_takes_to_eat_bananas <= h:
                # Now we must account for the possible new minimum value, if we found better one we update else we keep teh same 
                minimum_result_banana_per_hour = min(minimum_result_banana_per_hour, bananas_per_hour_possibly)

                # WE ALSO HAVE TO UPDATE OUR BINARY SEARCH ACCORDINGLY!!!
                right_pointer = bananas_per_hour_possibly - 1 
            else: 

                # Else the rate was too small, thus we need to check for a higher ratio 
                left_pointer = bananas_per_hour_possibly + 1 
        return minimum_result_banana_per_hour
        
        