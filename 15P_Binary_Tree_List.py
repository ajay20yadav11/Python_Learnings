# To create a Binary Tree using Python List


class BinaryTree:
    def __init__(self, size):
        self.customlist = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "Full"
        self.customlist[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "Done"


newBT = BinaryTree(10)
newBT.insertNode(20)
