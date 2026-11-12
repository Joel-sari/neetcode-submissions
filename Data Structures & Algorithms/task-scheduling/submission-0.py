"""
This is a good question for CPU, network and low level companies 




RETURN: the least number of units of times that the CPU will take to finish all the given tasks


- It is better to process the more frequent character first

We will us MaxHeap => will allow us to determine which task is the most frequent on in logn (log26 because there are only 26 tasks/characters)


We will also use queue => ((A tasks - one A tasked used), (Time when Task is avialble again))

we only add to back to Max Heap when the it is available (time avialble check eahc iteration)

We will also keep track of the time => (increment by 1 each time we pop from maxHeap, or idle)


when we get to task = 0, we don't have to process anymore, never has to be added to quuee anymore 

"""
from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        # remember counter creates a hashmap character : count 
        count_tasks = Counter(tasks)

        #now we want to store the counts into our MaxHeap
        # remember, in python heapify uses minheap, so we need to negate to get a MaxHeap Structure 
        maxHeap = [-count for count in count_tasks.values()]

        # orders it to maxHeap in O(n)
        heapq.heapify(maxHeap)

        # time increases by 1 as we go through each task + idle time 
        time = 0 

        # this will hold pairs [-count, idleTime] where idleTime = when is it next available
        queue = deque()

        # as long as both aren't empty we have more tasks to process, remmeber they will switch between each other
        while maxHeap or queue:
            
            # if it's not empty, that means we have tasks that could be run 
            if maxHeap:
                # we can pop and use it 
                # remember we have to update the count! and decrease 
                count = 1 + heapq.heappop(maxHeap)

                # if it isn't 0 then we can append to our queue
                if count: 
                    queue.append([count, time + n])

            # we need to now check our queue, we need to see if it has values and check if the last task added is withn in the time (idledTime/ cooldown period is done)
            if queue and queue[0][1] == time: 
                count, idleTime =  queue.popleft()
                heapq.heappush(maxHeap, count)


            time += 1 

        return time

        

        