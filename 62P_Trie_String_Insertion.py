"""
First we need to create a TrieNode which will act as a helper class to create a node inside a Trie tree.
Create a CHILDREN object to store a dictonary with string values or other.
Create a endofString with a boolean type to declare end of string or not
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofString = False


"""
Now to create a Trie Data Structures
create a class Trie
"""


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        current = self.root
        for anim in word:
            ch = anim
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.endofString = True
        print("Successfully Inserted")


newTrie = Trie()
newTrie.insertString("abc")
