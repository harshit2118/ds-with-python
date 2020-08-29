from BSTOperations import height
from BSTOperations.traversals import inorder
from BSTOperations.traversals import preorder
from BSTOperations.traversals import postorder
from BSTOperations import CL
##CLass for creating doubbly linklist
#LEFT---DATA---RIGHT
class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
##Inserting an element in
#BST
def InsertingBST(root,node):
    if root is None:
        root=Node
    else:
        if root.val<node.val:
            if root.right is None:
                root.right=node
            else:
                InsertingBST(root.right,node)
        else:
            if root.left is None:
                root.left=node
            else:
                InsertingBST(root.left,node) 
##Object creation and adding element in list                      
r=Node(60)
InsertingBST(r,Node(50))     
InsertingBST(r,Node(65))   
InsertingBST(r,Node(45))   
InsertingBST(r,Node(63))   
InsertingBST(r,Node(67))   
InsertingBST(r,Node(43))   
InsertingBST(r,Node(47))   
InsertingBST(r,Node(40))   
InsertingBST(r,Node(70))   
InsertingBST(r,Node(32))
print("Printing in InOrder")
inorder.Inorder(r) 
print("Printing in PreOrder")
preorder.Preorder(r)
print("Printing in PostOrder")
postorder.Postorder(r)
print("Height of a given Tree is {}".format(height.Height(r)))
print("Number of leaf nodes in a tree is {}".format(CL.CountLeaf(r)))