class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)

        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x > y:
                temp1 = (y - x)
                heapq.heappush(stones, temp1) 
            elif x < y:
                temp2 = (x - y)
                heapq.heappush(stones, temp2)
        
        if stones:
            return abs(stones[0])
        else:
            return 0
        


