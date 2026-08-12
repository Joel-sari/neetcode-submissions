class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # In python a minHeap is just an array 
        minHeap = []

        # remember for this loop it will get both points [0] and [1]
        for x, y in points:
            z_distance = (x ** 2) + (y ** 2)
            minHeap.append([z_distance, x, y ])
        
        # then we need to sort our min heap using python's built in heapify 
        heapq.heapify(minHeap)

        # k closest points to origin 
        result = []
        while k > 0: 
            z_distance, x, y = heapq.heappop(minHeap)
            result.append([x, y]) 
            k -= 1
        return result




        