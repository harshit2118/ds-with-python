def CountLeaf(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    else:
        return CountLeaf(node.left)+CountLeaf(node.right)