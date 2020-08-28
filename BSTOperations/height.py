def Height(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 0
    else:
            h1=Height(node.left)
            h2=Height(node.right)  
            return 1+max(h1,h2)