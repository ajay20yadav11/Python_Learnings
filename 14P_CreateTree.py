#Tree Terminoloy

class TreeNode:
    def __init__ (self, data, children=[]):
        self.data = data
        self.children = children

    def __str__(self, level=0):
        ret = " " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def addChild(self, TreeNode_value):
        self.children.append(TreeNode_value)


tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hots = TreeNode('Hots', [])
tree.addChild(cold)
tree.addChild(hots)

print(tree)
