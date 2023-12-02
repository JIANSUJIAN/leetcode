#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Approach 1: Linear Time
# Time: O(N) 
# Space: O(d) = O(logN) to keep the recursion stack, where d is the tree depth
# class Solution:
#     def countNodes(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         else:
#             return 1 + self.countNodes(root.right) + self.countNodes(root.left)

# Approach 2: Binary search
# Time: O(d^2) = O(log^2(N))
# Space: O(1)

class Solution:
    def count_depth(self, node: TreeNode) -> int:
        """
        Return the tree depth in O(d) time
        """
        d = 0
        while node.left:
            d += 1
            node = node.left
        return d
    
    def exist(self, idx: int, d: int, node: TreeNode) -> bool:
        """
        Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        Return True if last level node idx exists.
        Binary search with O(d) complexity. 
        """

        left, right = 0, 2**d - 1
        for _ in range(d):
            pivot = left + (right - left) // 2
            if idx <= pivot:
                # Move right boundary to pivot. Since nodes are filled from left to right,
                # if a node at 'pivot' index doesn't exist, no nodes exist to its right.
                right = pivot
                node = node.left
            else:
                # Move left boundary to 'pivot + 1' to narrow the search to the right half.
                # This avoids redundancy and ensures the search progresses correctly.
                left = pivot + 1
                node = node.right
        return True if node else False
    

    def countNodes(self, root: Optional[TreeNode]) -> int:

        # If the tree is empty
        if not root:
            return 0
        
        # If the tree contains 1 node
        d = self.count_depth(root)
        if d == 0:
            return 1
        
        # Last level nodes are enumerated from 0 to 2**d - 1 (left -> right).
        # Perform binary search to check how many nodes exist.
        left, right = 1, 2**d - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if self.exist(pivot, d, root):
                # If node exists at 'pivot', continue search in the right half
                left = pivot + 1
            else:
                # If node does not exist at 'pivot', continue search in the left half
                right = pivot - 1
        
        # The tree contains 2**d - 1 nodes on the first (d - 1) levels
        # and `left` nodes on the last level.
        return (2**d - 1) + left


                






# @lc code=end

