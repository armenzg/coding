'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True

 

Example 2:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def insert(self, val: int) -> None:
        if not (val == self.val) and val:
            if val < self.val:
                if self.left:
                    self.left.insert(val)
                else:
                    self.left = TreeNode(val)
            else:
                if self.right:
                    self.right.insert(val)
                else:
                    self.right = TreeNode(val)
    

def in_order_array(root: TreeNode) -> list:
    a = []
    if root.left:
        foo = in_order_array(root.left)
        a = a + foo
    a.append(root.val)
    if root.right:
        a = a + in_order_array(root.right)
    return a

class Solution:
    def findTarget(self, root: TreeNode, target: int) -> bool:
        result = False
        ordered_list = in_order_array(root)
        # Start evaluating from greatest value (at the end of the list)
        for i in range(len(ordered_list)-1, 0, -1):
            num = ordered_list[i]
            for j in range(i-1):
                small_num = ordered_list[j]
                if target == num + small_num:
                    result = True
                    break
        print("true" if result else "false")
        return result
    
a = TreeNode(5)
a.insert(3)
a.insert(2)
a.insert(4)
a.insert(6)
a.insert(7)
sol = Solution()
assert sol.findTarget(a, 9) == True
assert sol.findTarget(a, 28) == False

b = TreeNode(0)
b.insert(-1)
b.insert(-4)
b.insert(4)
b.insert(None)
print(in_order_array(b))
assert sol.findTarget(b, -4) == True