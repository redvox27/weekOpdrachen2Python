from collections import namedtuple

Node = namedtuple('Node', 'data left right')

node1 = Node(data=7, left=None, right=None)

tree = Node(1,
            Node(2,
                 Node(4,
                      Node(7, None, None),
                      None),
                 Node(5, None, None)),
            Node(3,
                 Node(6,
                      Node(8, None, None),
                      Node(9, None, None)),
                 None))

numArray = []
print(tree.left)
print(tree.right)
def preorder(tree):
    numArray.append(tree.data)
    if tree.left:
        preorder(tree.left)
    if tree.right:
        preorder(tree.right)

preorder(tree)
print(sorted(numArray))