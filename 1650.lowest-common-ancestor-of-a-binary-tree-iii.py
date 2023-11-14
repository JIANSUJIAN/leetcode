#
# @lc app=leetcode id=1650 lang=python3
#
# [1650] Lowest Common Ancestor of a Binary Tree III
#

# @lc code=start

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # Initialize two pointers, a and b, to nodes p and q respectively.
        a, b = p, q
        
        # Traverse the tree up towards the root using parent pointers.
        # The idea is to use two pointers, one starting at p and the other at q. 
        # Both pointers traverse up the tree, but when one reaches the root (None), it continues from the other node.
        # Eventually, they will meet at the lowest common ancestor.
        while a != b:
            # If 'a' reaches the root, start traversing from node 'q'.
            if not a:
                a = q
            else:
                a = a.parent
            
            # If 'b' reaches the root, start traversing from node 'p'.
            if not b:
                b = p
            else:
                b = b.parent
        
        # Return the node where both pointers met, i.e., the lowest common ancestor.
        return a 


        
# @lc code=end

