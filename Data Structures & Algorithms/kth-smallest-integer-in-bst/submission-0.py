# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sorted_array = []

        def inorderTraversal(root):

            if not root: 
                return 
            inorderTraversal(root.left)
            sorted_array.append(root.val)
            inorderTraversal(root.right)
            return sorted_array
        
        return inorderTraversal(root)[k -1]
        