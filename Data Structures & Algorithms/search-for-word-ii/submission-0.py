

class TrieNode: 
    def __init__(self): 
        self.children = {}
        self.end_of_word = False

    def addWord(self, word): 
        current = self
        for character in word: 
            if character not in current.children: 
                current.children[character] = TrieNode()
            current = current.children[character]


        current.end_of_word = True 


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # creating a root trie node 
        root = TrieNode() 

        # we are creating out prefix tree with the list of words given to us 
        for word in words: 
            root.addWord(word)


        ROWS, COLS = len(board), len(board[0])

        # result => is a set to avoid duplicate words
        # visit => checks to see if we already visited the word while we our running our dfs algorithm
        result, visit = set(), set()

        def dfs(row, col, node, word): 

            # this is if our base case, if nothing we fail going out of bounds or we have visited the node before or the node value doesn't have the same character that the board holds
            if ( row < 0 or 
                 col < 0 or 
                 row == ROWS or 
                 col == COLS or 
                 (row, col) in visit or 
                 # maybe the board[row][not in our current trie]
                 board[row][col] not in node.children):
                 return

            
            visit.add((row, col))
            # okay so now we are updating our values since we will check the next trie node

            node = node.children[board[row][col]]
            
            # this is the word we are constructing, and eventually adding to our result set
            word += board[row][col]

            # if this is the end of the word, we can add the constructed word into our result set 
            if node.end_of_word: 
                result.add(word)

            
            #finally, after all the checking and updating of our "pointers", we can run our search recursively 
            dfs(row + 1, col, node, word) # right
            dfs(row, col + 1, node, word) # down
            dfs(row - 1, col, node, word) # left 
            dfs(row, col - 1, node, word) # up

            visit.remove((row, col))



        #since we are backtracking we need to remove it from visited, like popping the node afyter visiting the full in depth path. 
        for row in range(ROWS): 
            for col in range(COLS): 
                dfs(row, col, root, "")


        return list(result)


            



            



        