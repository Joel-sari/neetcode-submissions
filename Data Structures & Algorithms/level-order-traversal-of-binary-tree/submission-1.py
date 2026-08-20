# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        leveled_list = []
        queue = deque()
        if root: 
            queue.append(root)

        while queue: 
            level_array = []
            for i in range(len(queue)):
                current_node = queue.popleft()
                level_array.append(current_node.val) 
                if current_node.left: 
                    queue.append(current_node.left)
                if current_node.right: 
                    queue.append(current_node.right)
            leveled_list.append(level_array)
        return leveled_list

        