from LinkListOperations import PrintNode
class Node:
    def __init__(self,key):
        self.data=key
        self.next=None
def Insert(head,node):
    if head==None:
        head=node
    else:
        if head.next is None:
            head.next=node
        else:
            Insert(head.next,node)
h=Node(10)
Insert(h,Node(30))
Insert(h,Node(40)) 
Insert(h,Node(50)) 
Insert(h,Node(60)) 
Insert(h,Node(70)) 
Insert(h,Node(80))
print("The list is {}".format(PrintNode.PrintLL(h)))                      