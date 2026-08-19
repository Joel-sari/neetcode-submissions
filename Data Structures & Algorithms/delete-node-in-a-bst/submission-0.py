# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: 
            return None
        if key > root.val: 
            root.right = self.deleteNode(root.right, key)

        elif key < root.val: 
            root.left = self.deleteNode(root.left, key)

        else: 
            # Case in which we have either a child or no child at all (Just plug and play lowkey)
            if not root.left: 
                return root.right
            elif not root.right: 
                return root.left 
            # If both are checks fail, this means that we have two children and need to handle it delicately
            else:
                successor_to_root = self.findMin(root.right)
                root.val = successor_to_root.val
                root.right = self.deleteNode(root.right, successor_to_root.val)
        return root 





    def findMin(self, root): 
        current = root
        while current and current.left: 
            current = current.left 
        return current

        