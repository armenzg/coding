# https://www.youtube.com/watch?v=oSWTXtMglKE
class Node(object):
    def __init__(self, value: int) -> None:
        self.data = value
        self.left = None
        self.right = None
    
    def insert(self, value: int) -> None:
        if (value == self.data):
            return
        elif (value < self.data):
            if not self.left:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = Node(value)
            else:
                self.right.insert(value)
    
    def contains(self, value: int) -> bool:
        if (value == self.data):
            return True
        elif (value < self.data):
            if not self.left:
                return False
            else:
                self.left.contains(value)
        else:
            if not self.right:
                return False
            else:
                self.right.contains(value)
    
    def print_in_order(self) -> None:
        def _print_in_order(node) -> None:
            if node.left:
                _print_in_order(node.left)
            print(node.data)
            if node.right:
                _print_in_order(node.right)

        _print_in_order(self)
    
    def in_order_printing(self) -> str:
        def _in_order_printing(node) -> str:
            # In-order A B C
            tree_str = ""
            if node.left:
                tree_str += "{}".format(_in_order_printing(node.left))

            if not node.left:
                tree_str += str(node.data)
            else:
                tree_str += " {}".format(node.data)

            if node.right:
                tree_str += " {}".format(_in_order_printing(node.right))

            return tree_str
        
        print(_in_order_printing(self))
    
    def pre_order_printing(self) -> str:
        def _pre_order_printing(node) -> str:
            # Pre-order B A C
            tree_str = str(node.data)
            if node.left:
                tree_str += " {}".format(_pre_order_printing(node.left))

            if node.right:
                tree_str += " {}".format(_pre_order_printing(node.right))

            return tree_str
        
        print(_pre_order_printing(self))
    
    def post_order_printing(self) -> str:
        def _post_order_printing(node) -> str:
            # Post-order A C B
            tree_str = ""
            if node.left:
                tree_str += "{} ".format(_post_order_printing(node.left))
            if node.right:
                tree_str += "{} ".format(_post_order_printing(node.right))
            tree_str += str(node.data)

            return tree_str
        
        print(_post_order_printing(self))
    
    # Based on https://www.hackerrank.com/challenges/tree-level-order-traversal/problem
    def level_traversing(self):
        from collections import defaultdict
        # The hashses are going to be the levels
        hash_map = defaultdict(list)

        def _level_traversing(root, level):
            hash_map[level].append(root.data)
            if root.left:
                _level_traversing(root.left, level + 1)
            if root.right:
                _level_traversing(root.right, level + 1)

        _level_traversing(self, 0)
        flat_list = []
        for level in sorted(hash_map.keys()):
            flat_list += hash_map[level]

        print(' '.join(map(lambda x: str(x), flat_list)))

if __name__ == "__main__":
    tree = Node(8)
    tree.insert(2)
    tree.insert(9)
    tree.insert(7)
    assert tree.contains(8)
    tree.print_in_order()
    # These print all in one line
    tree.in_order_printing()
    tree.pre_order_printing()
    tree.post_order_printing()
    tree.level_traversing()