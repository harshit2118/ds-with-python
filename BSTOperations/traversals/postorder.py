##Displaying in preorder
# root_left_right
def Postorder(root):
    if root:
        Postorder(root.left)
        Postorder(root.right)
        print(root.val)