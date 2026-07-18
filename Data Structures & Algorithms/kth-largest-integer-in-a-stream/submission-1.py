class KthLargest:

    """
    This is lowkey kinda hard, we need to understand what it means to be the kth biggest:

    My initial thought = "sort reversethe algorithm and then find the kth largest by going backwards in the index"


    However there is a better way to do it using a priority queue or a min heap!, where we only include numbers that are largest all the way down 
    to the "minimum" which is the top of of the min heap and the kth largest value !, it is just more efficient

    Our first task is to fix the constructor to take the array and make it a min heap 


    """ 

    def __init__(self, k: int, nums: List[int]):
        # minheap with k largest intergers

        self.minHeap = nums
        self.k = k

        # In python this is how you turn an array into a min heap, by default it is a minheap
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            # heap pop removes the minimum value UNTIL our length reaches n - k, it then just maintains it's structure
            heapq.heappop(self.minHeap)
        

    def add(self, val: int) -> int:

        # we are adding the neew value, and then just keeping the minheap shape
        heapq.heappush(self.minHeap, val)

        # We don't want to pop if we are under k number of elements!!
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # the value at the first position in a min heap is always the smallest value.
        return self.minHeap[0]
        
