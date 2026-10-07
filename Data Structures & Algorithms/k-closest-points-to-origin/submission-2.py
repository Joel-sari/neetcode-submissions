class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        result = []

        for x, y in points:
            euclidean = math.sqrt((x ** 2) + (y ** 2))
            heapq.heappush(heap, (euclidean, [x,y]))
        
        while k > 0:
            temp = heapq.heappop(heap)
            result.append(temp[1])
            k -= 1
        return result


