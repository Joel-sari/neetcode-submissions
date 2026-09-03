"""
EVERY TREE NODE OBJECT WILL HAVE 

CHILDREN = { "character" : TrieNodeObject } 

ONE OBJECT PER CHARACTER! 
"""

class TrieNode: 
    def __init__(self): 
        # we can have MANY children
        self.children = {}
        self.endOfWord = False 

        # NOTE THE character isn't a part of the constructor as it's own thing

class PrefixTree:
    # First we should initialie our TrieNode
    def __init__(self):
        # we start of our empty root Node 
        self.root = TrieNode()
    def insert(self, word: str) -> None:

        # set up a pointer for our nodes 
        current_pointer = self.root 
        # we are going to go character by character, check to see whether its exists already 
        for character in word: 
            # if it isn't in our hashmap yet, it means that the trie node character doesn't exist, so lets creat a new one in our hashmap!
            if character not in current_pointer.children:
                current_pointer.children[character] = TrieNode()

            # if already exists we can skip the step above, else if we didn't we would just go through the Trie Node we just made and keep making new TrieNodes
            current_pointer = current_pointer.children[character]
        
        #after finishing the for loop, our current will be the object TrieNode of the last character
        current_pointer.endOfWord = True
                
    def search(self, word: str) -> bool:

        current_pointer = self.root 
        for character in word: 
            if character not in current_pointer.children: 
                return False

            

            current_pointer = current_pointer.children[character]

        # Why this is neccesary instead of just returning True is cause there is a chance we search for app, and we have apples, basically we wouldn't have app in our Trie Tree

        return current_pointer.endOfWord 
        

    def startsWith(self, prefix: str) -> bool:


        current_pointer = self.root 
        for character in prefix: 
            if character not in current_pointer.children: 
                return False

            

            current_pointer = current_pointer.children[character]

        # Now we can just return True as long as the whole loop runs, it doesn't matter if we are at the end
        return True
        
        