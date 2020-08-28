##Displaying in inorder
# left_root_right
def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.val)
        Inorder(root.right)