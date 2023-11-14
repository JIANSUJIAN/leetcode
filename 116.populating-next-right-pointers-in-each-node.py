#
# @lc app=leetcode id=116 lang=python3
#
# [116] Populating Next Right Pointers in Each Node
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

## 1
## Traverse
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # Base Case: If the tree is empty, simply return None
        if root is None:
            return None
        
        # Start connecting nodes from one level below the root
        self.traverse(root.left, root.right)
        return root
    
    def traverse(self, node1: 'Node', node2: 'Node'):
        # Base Case: If any of the nodes is None, just return
        # This is because we are dealing with a perfect binary tree; if one node is None, the other must be None too.
        if node1 is None or node2 is None:
            return 

        # Connect node1 to node2
        node1.next = node2

        # Connect the children of node1 (i.e., left child to right child)
        self.traverse(node1.left, node1.right)
        # Connect the children of node2 (i.e., left child to right child)
        self.traverse(node2.left, node2.right)
        
        # Connect the right child of node1 to the left child of node2
        # This is crucial because node1 and node2 are on the same level but are children of different parents
        self.traverse(node1.right, node2.left)


        
# @lc code=end

