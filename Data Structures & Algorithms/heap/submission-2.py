class MinHeap:

    # Remember, "children" is 2* i and 2*i + 1
    
    def __init__(self):
        self.heap = [0] # dummy value
        # the first spot in our array will just a dummy 0

        

    def push(self, val: int) -> None:
        self.heap.append(val)

        last_index_in_array = len(self.heap) - 1 #
        
        # bubble up which essentially swaps the parent node if needed to keep the minheap property
        
        self.bubble_up(last_index_in_array)


    def pop(self) -> int:
        # we want to return the smallest value 
        if len(self.heap) <= 1: 
            return -1 
        if len(self.heap) == 2: 
            return self.heap.pop()

        # remember, popping will give us the min value, thus we could swap the root of out minheap tree with the furthest leaf node, and then pop the 1, and finally bubble down to fix the structure of the tree
        
        # save the root value
        root = self.heap[1]

        # now overwrite root with last value in heap 
        self.heap[1] = self.heap.pop()

        self.bubble_down(1) # bubble down from the root

        return root

    def top(self) -> int:
        # if our length is more than just our dummy node!
        return self.heap[1] if len(self.heap) > 1 else -1
        

    def heapify(self, nums: List[int]) -> None:
        
        self.heap = [0] + nums

        for i in range(len(self.heap) // 2, 0, -1):
            self.bubble_down(i)


    def bubble_up(self, index): 
        # parent is i // 2
        parent = index // 2 

        # while the child value is less than the parent, meaning we need to move it up to handle the minheap structure
        while index > 1 and self.heap[index] < self.heap[parent]: 
            # here we are swapping their values 
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]

            # update our "pointer"
            index = parent
            parent = index // 2

    
    def bubble_down(self, index): 
        num_of_elems = len(self.heap)
        
        while 2 * index < num_of_elems:
            #left child 
            left_child = 2 * index 
            right_child = left_child + 1

            # current smallest
            current_smallest = left_child
            if right_child < num_of_elems and self.heap[right_child] < self.heap[left_child]: 
                current_smallest = right_child 

            # if our heap property is satisfied => parent val < smallest_child_val < other child_val 
            parent_val = self.heap[index]
            if parent_val <= self.heap[current_smallest]: 
                return 

            #else we can apply the swap, and update out parent and child pointers
            self.heap[current_smallest], self.heap[index] = self.heap[index], self.heap[current_smallest]
            
            index = current_smallest 
            

            


        
    

            
        