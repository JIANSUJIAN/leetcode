#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.

from typing import Optional
from queue import Queue

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # If the tree is empty, then its minimum depth is 0
        if not root:
            return 0
        
        # Initialize a queue to facilitate level-by-level traversal
        q = Queue()
        
        # Enqueue the root node to start BFS traversal
        q.put(root)
        
        # Initialize depth counter, root node is at depth 1
        depth = 1  

        # Continue processing while there are nodes in the queue
        while q:
            # Get the number of nodes at the current depth level
            sz = q.qsize()

            # Process each node at the current depth level
            for i in range(sz):
                # Dequeue the next node for processing
                cur = q.get()

                # Check if the current node is a leaf node (no children)
                # If it is, we've found the shortest path to a leaf and return the depth
                if not cur.left and not cur.right:
                    return depth
                
                # If the current node has a left child, enqueue it for processing
                if cur.left:
                    q.put(cur.left)
                
                # If the current node has a right child, enqueue it for processing
                if cur.right:
                    q.put(cur.right)
            
            # Increment the depth counter since we move to the next depth level in the next iteration
            depth += 1
        
        # This line is technically unreachable in a well-formed binary tree
        # because the function would have returned upon finding a leaf node.
        # However, it's kept here for completeness.
        return depth


        
# @lc code=end

