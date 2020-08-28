##Displaying in preorder
# root_left_right
def Preorder(root):
    if root:
        print(root.val)
        Preorder(root.left)
        Preorder(root.right)