class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # We sort the 
        intervals.sort(key=lambda x: x[0])

        #The list of lists that we will be returning 
        output = [intervals[0]] # we will initialize it with an initilal interval, why?

        # Well our algorithm consists of us adding the interval but ofc before adding we want to make sure it isn't conflicting!


        # By looping through it like this we are basically saying 
        # we the start will hold the the index 0 val and end will hold the index 1 value of each interval starting at 1 until the end 
        for start, end in intervals[1:]:
            # -1 gives us the last interval in the ouput and the 1 gives us the end time of that interval
            last_interval_addeds_end_time = output[-1][1]

            # if the start of the interval we want to insert collides with the last interval added into out put 
            # aka meaning the one before it 
            if start <= last_interval_addeds_end_time:
                # using the previous interval's start time and the current meeting end 
                last_interval_addeds_start_time = output[-1][0]

                
                # We now have to determine which of the two meetings ends the latest
                # which means that whiever has a higher value for the end index
                end_of_new_interval = max(last_interval_addeds_end_time, end )

                # We are now modifying the last intervals end value instead of replacing or adding a new one cuase remember
                # we initially added the thing already thus, we would either have to remove and add a while new one but that doesn;t reeally have to happned
                output[-1][1] = end_of_new_interval 
            else:
                output.append([start, end])

        return output
