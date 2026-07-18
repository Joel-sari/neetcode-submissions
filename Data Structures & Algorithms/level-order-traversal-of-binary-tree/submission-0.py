# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


"""
Basically this is just an example of a breadth first search
Please pay attention on how it is implemented!!!
"""

class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left 

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:


        #This is how we initiliaze a queue like structure in python
        queue = collections.deque()

        # This will have the array of arrays
        result = []
        # we append root into our queue
        queue.append(root)

        while queue:

            # we get the length of the queue, current length of the queue, note tghis is essential
            #In keeping track of the number of nodes in the current level
            queue_length = len(queue)
            level = []

            for i in range(queue_length): 
                node_in_level = queue.popleft()

                # Note it is possinle for a node to be null so we must ONLY add those that have a value 
                # NOTE THAT the WAY we are CHECKING will still append NULLS to the queue but wont necessarily
                # append its values left or right and will just keep poppimg till the queue is empty and then exit out the while loop
                if node_in_level:
                    level.append(node_in_level.val)
                    queue.append(node_in_level.left)
                    queue.append(node_in_level.right)

                # we need to check for empty lists, which can occur 
            if level: 
                result.append(level)
        
        return result 


        


        