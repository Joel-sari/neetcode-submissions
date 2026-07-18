class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key 
        self.val = val 
        self.left = None
        self.right = None 

        
class TreeMap:
    
    def __init__(self):
        # This will hold the first node in our BST (initially our tree is empty)
        self.root = None


    def insert(self, key: int, val: int) -> None:

        # we are creating a new node with the value that we want to insert in our tree
        newTreeNode = TreeNode(key, val)
        if self.root is None: 
            self.root = newTreeNode
            return
        

        #  current_tree_node should start at the root!
        # and then we should update the pointer based of off that 
        current_tree_node  = self.root        
        while True:
            if key < current_tree_node.key:
                if current_tree_node.left == None:
                    current_tree_node.left = newTreeNode
                    return 
                current_tree_node = current_tree_node.left
            elif key > current_tree_node.key: 
                if current_tree_node.right == None:
                    current_tree_node.right = newTreeNode
                    return 
                current_tree_node = current_tree_node.right
            else: 
                # if we already have this key in our BST, then we just replace the 
                # value at that key rather than
                current_tree_node.val = val
                return 

    def get(self, key: int) -> int:
        current_tree_node = self.root
        while current_tree_node != None:
            if key < current_tree_node.key :
                current_tree_node = current_tree_node.left 
            elif key > current_tree_node.key :
                current_tree_node = current_tree_node.right
            else:
                return current_tree_node.val
        return -1
                


    def getMin(self) -> int:
        # getMin is very similar to the getMax function
        current_tree_node = self.root 
        while current_tree_node and current_tree_node.left:
            current_tree_node = current_tree_node.left
        return current_tree_node.val if current_tree_node else -1

    def findMin(self, node):
        while node and node.left:
            node = node.left 
        return node

    # Goal is to return a value and go to the max key 
    def getMax(self) -> int:
        current_tree_node = self.root
        
        # Why do we also check current_tree_node itself?? cause it is possible that it's null! 
        #so we need to account for it too
        while current_tree_node and current_tree_node.right:
            current_tree_node = current_tree_node.right 

        #if it is null then we need to ensure that we return the VALUE -1, not the null itself
        # and we need to make sure again that we are returning the value not the key or the object itself
        return current_tree_node.val if current_tree_node else -1

        

    def remove(self, key: int) -> None:
        # removing recursively is the easiest way!
        self.root = self.removeHelper(self.root, key)
    

    # Removes the node with key and returns the new ROOT of the subtree
    def removeHelper(self, current, key):

        # we need to figure out the base case! 
        if current is None:
            return None
            #So we return None if we dont have a node to remove since it don't exist

        if key > current.key:
            current.right = self.removeHelper(current.right, key) 
            # we need to ASSIGN the deletion in case we delete something and we need it to show
            # / return the new subtree on the right side
        elif key < current.key:
            current.left = self.removeHelper(current.left, key)
            # we need to ASSIGN the deletion in case we delete something and we need it to show
            # / return the new subtree on the left side
        else:
            # if the current_node has no left child?? well we can just replace that node
            # with it's right child/subtree we replace it and set that to be the new right
            if current.left is None:
                return current.right 
            # if the current node has no right child? well now we can replace that node with
            # with it's left child/subtree we replace it and set that to be the new current's left
            elif current.right is None:
                return current.left 


            else: 
                # we can swap the current with the inorder successor!! basically by swapping the tree node we want to delete 
                # with the successor, we ensure that proper BST behaviour remains intact
                successor = self.findMin(current.right)
                
                # Basically here we are setting our current node's value (the one we want deleted) to the successors key and value 
                current.key = successor.key 
                current.val = successor.val 


                #Okay but after we run the above, what have we done exactly? We now just have two identical nodes 
                # with the same key and value 
                
                # So how do we remove the extra node we dont want? well we can just recursively call our own function 
                # to remove it, (which it will do the if removal since it has no left child), remember to use curr.right so we dont remove the node we just changed 
                current.right = self.removeHelper(current.right, successor.key)
        
        return current






 
    
    
    def getInorderKeys(self) -> List[int]:
        result = [] # this is an array that holds the array of tree values in an in order traversalish wya 
        self.inorderTraversal(self.root,result)

        return result
        
    
    # creating a helper function for recursion and in order traversal 
    def inorderTraversal(self, root, result):

        if root: 
            self.inorderTraversal(root.left, result)
            # appending to our result array if we reach the bottom of the left, 
            result.append(root.key)
            self.inorderTraversal(root.right, result)



