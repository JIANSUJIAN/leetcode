#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # List to store the final level order traversal result
        res = []
        
        # If the tree is empty, return an empty list
        if not root:
            return res
        
        # Initialize a queue to facilitate level-by-level traversal
        q = []
        
        # Enqueue the root node to start the level order traversal
        q.append(root)

        # Continue processing while there are nodes in the queue
        while q:
            # Get the number of nodes at the current depth level
            sz = len(q)
            
            # List to store values of nodes at the current depth level
            level = []

            # Process each node at the current depth level
            for i in range(sz):
                # Dequeue the next node for processing
                cur = q.pop(0)
                
                # Add the current node's value to the level list
                level.append(cur.val)

                # If the current node has a left child, enqueue it for future processing
                if cur.left:
                    q.append(cur.left)
                
                # If the current node has a right child, enqueue it for future processing
                if cur.right:
                    q.append(cur.right)
            
            # After processing all nodes at the current depth level, 
            # add the level list to the final result
            res.append(level)
        
        # Return the final level order traversal result
        return res



# @lc code=end

