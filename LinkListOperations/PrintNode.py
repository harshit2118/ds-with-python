def PrintLL(node):
    if node:
      print(node.data)
      if node.next is not None:
        PrintLL(node.next)
        