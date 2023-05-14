class CreateNode:
    def __init__(self, value):
        self.value = value
        self.leftvalue = None
        self.rightvalue = None


def InsertNode(TreeNode, NodeValue):
    if TreeNode.value == None:
        TreeNode.value = NodeValue
    elif NodeValue <= TreeNode.value:
        TreeNode.leftvalue = CreateNode(NodeValue)


new = CreateNode(8)
print(new.value)
InsertNode(new, 6)
print(new.value)
