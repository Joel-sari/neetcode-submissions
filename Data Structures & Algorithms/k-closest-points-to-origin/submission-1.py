class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minheap = []

        for x, y in points: 
            z = x**2 + y**2

            minheap.append([z,x,y])

        heapq.heapify(minheap)

        output = []
        while k > 0:
            z, x, y = heapq.heappop(minheap)
            output.append([x, y])

            k-= 1

        return output

        