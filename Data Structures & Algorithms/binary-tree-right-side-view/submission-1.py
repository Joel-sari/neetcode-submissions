# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        right_viewed_nodes = []
        queue = deque()
        

        if root: 
            queue.append(root)

        
        while queue: 
            current_node = 0
            for i in range(len(queue)): 
                current_node = queue.popleft()

                if current_node.left:
                    queue.append(current_node.left)

                if current_node.right:
                    queue.append(current_node.right)

            right_viewed_nodes.append(current_node.val)
        
            




        return right_viewed_nodes


        