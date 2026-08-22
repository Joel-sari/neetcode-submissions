class Solution:
    def lastStoneWeight(self, stones: List[int])-> int: 

        # NOTE, python requires you to negate the values inside the heap to actually use it's max heapify
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1: 
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            

            if y > x: 
                heapq.heappush(stones, x - y)
        
        # what if we had no stones left?? we add a zero stone do handle the edge case
        stones.append(0)

        return abs(stones[0])

            


                
            


