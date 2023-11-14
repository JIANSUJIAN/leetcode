#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
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

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # If the tree is empty, return None immediately.
        if not root:
            return None
        
        # Initialize a queue to facilitate BFS (level-by-level traversal).
        # Start by adding the root node to the queue.
        q = [root]

        # Continue processing as long as there are nodes in the queue.
        while q:
            # Determine the number of nodes at the current depth level.
            # This helps in identifying when we are processing the last node of the current level.
            sz = len(q)
            
            # Process each node at the current depth level.
            for i in range(sz):
                # Dequeue the next node for processing.
                cur = q.pop(0)
                
                # If this isn't the last node at this level, 
                # point its 'next' to the node that's at the front of the queue.
                if i < sz - 1:
                    cur.next = q[0]
                
                # If the current node has a left child, enqueue it for processing in the next iteration.
                if cur.left:
                    q.append(cur.left)
                
                # Similarly, if the current node has a right child, enqueue it for processing.
                if cur.right:
                    q.append(cur.right)
        
        # Return the root of the tree after setting all 'next' pointers.
        return root


        
# @lc code=end

