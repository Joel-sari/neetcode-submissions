class TreeNode:
    def __init__(self, val=0, left= None, right= None):
        self.val = val 
        self.right = right
        self.left = left 


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        # we use the tuple to signify # (node, column), NOTE, dont get confused with the multiple (), right now we are just saying we are making a list with tuples
        # Why tuples? Well because we iwll use a hashmap, thus hashes only allow tuples for keys!
        queue = deque([(root, 0)])

        # we will also keep track of the minumum column and maximum column to later "loop through our dicitionary"

        minimum_column, maximum_column = 0 , 0 

        # again remember that thhis hashmap  creates a has of list
        columns_to_node_vals = defaultdict(list)

        # while we have values in our queue , again this is typical for BFS !
        while queue:
            node, column = queue.popleft() # this gives us our node and col 

            # each time we iterate through, we update our new min and max columns 
            minimum_column, maximum_column = min( minimum_column, column), max( maximum_column, column)


            # now we need to also append this node.val we come across into the according column key 
            columns_to_node_vals[column].append(node.val)


            # Now we need to add the node tuple pair into our queue and disect it's values!

            # if the node to the left exists, let's append to our queue so we can check later on it's value and column and map into our dicitonary 
            if node.left: 
                queue.append((node.left, column -1))
            if node.right: 
                queue.append((node.right ,column + 1))


        # LASTLY we need to iterate through our hashmap and return a list of lists 
        # you'll notice that keeping track of these columns allowed us to set up a range that goes in order!!! whcih is essential for how they want us to return the values, 
        # remember that the tree columns will alwyas be continguous 
        return [columns_to_node_vals[column] for column in range(minimum_column, maximum_column + 1) ]






        