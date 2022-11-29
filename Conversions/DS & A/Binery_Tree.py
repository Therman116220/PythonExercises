
class Node:

 def __init__(self, value):

        self.data = value
        self.left = None
        self.right = None

def bfs(root_node):
     queue = []
     if root_node:
          queue.append(root_node)
     while queue:
         cur_node = queue.pop(0)
         print(cur_node.data, end=" ")
         if cur_node.left:
             queue.append(cur_node.left)
         if cur_node.right:
             queue.append(cur_node.right)


if __name__ == '__main__':
     root = Node(1)
     root.left = Node(2)
     root.right = Node(3)
     root.left.left = Node(4)
     root.left.right = Node(5)
     root.right.left = Node(6)
     root.right.right = Node(7)
     '''print(root)'''
     bfs(root)


     print(root.left)
     print(root.right)
     print(root.left.left)
     print(root.left.right)
     print(root.right.left)
     print(root.right.right)
     print(root.left.left.left)
     print(root.left.left.right)
     print(root.left.right.left)
     print(root.left.right.right)




