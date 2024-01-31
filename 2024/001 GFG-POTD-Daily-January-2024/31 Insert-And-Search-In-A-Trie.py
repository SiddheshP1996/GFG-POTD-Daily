# User function Template for python3

"""
class TrieNode: 
      
    def __init__(self): 
        self.children = [None]*26
  
        # isEndOfWord is True if node represent the end of the word 
        self.isEndOfWord = False
"""

class Solution:
    # Function to insert string into TRIE.
    def insert(self, root, key):
        # Code here
        current_node = root
        for character in key:
            if current_node.children[ord(character) - ord("a")] == None:
                new_node = TrieNode()
                current_node.children[ord(character) - ord("a")] = new_node
            current_node = current_node.children[ord(character) - ord("a")]
        current_node.isEndOfWord = True
    
    # Function to use TRIE data structure and search the given string.
    def search(self, root, key):
        # Code here
        current_node = root
        for character in key:
            if current_node.children[ord(character) - ord("a")] == None:
                return False
            current_node = current_node.children[ord(character) - ord("a")]
        return current_node.isEndOfWord
