# https://www.hackerrank.com/challenges/tree-level-order-traversal/problem

# Hackerrank code begins
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break
# Hackerrank code ends

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
from collections import defaultdict
# The hashses are going to be the levels
hash_map = defaultdict(list)
def levelOrder(root):
    _level_traversing(root, 0)
    flat_list = []
    for level in sorted(hash_map.keys()):
        flat_list += hash_map[level]

    result = ' '.join(map(lambda x: str(x), flat_list))
    print(result)  # Hacker rank looks at stdout
    return result

def _level_traversing(root, level):
    hash_map[level].append(root.info)
    if root.left:
        _level_traversing(root.left, level + 1)
    if root.right:
        _level_traversing(root.right, level + 1)

# Hackerrank code begins
tree = BinarySearchTree()
t = int('6')

arr = list(map(int, '1 2 5 3 6 4'.split()))

for i in range(t):
    tree.create(arr[i])

assert levelOrder(tree.root) == '1 2 5 3 6 4'
# Hackerrank code ends