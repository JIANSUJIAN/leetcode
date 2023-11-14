#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.


from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # List to store the final zigzag level order traversal result
        res = []

        # Base condition: if the tree is empty, return an empty list
        if not root:
            return res

        # Initialize a queue to facilitate level-by-level traversal
        q = []
        q.append(root)

        # Flag to determine the direction of zigzag traversal. 
        # If True, left to right. If False, right to left.
        flag = True

        # Continue processing while there are nodes in the queue
        while q:
            # Get the number of nodes at the current depth level
            sz = len(q)

            # Use deque to easily append elements from both ends
            level = deque()

            # Process each node at the current depth level
            for i in range(sz):
                # Dequeue the next node for processing
                cur = q.pop(0)

                # If flag is True, append node value from the right; 
                # otherwise, append from the left for reverse order
                if flag:
                    level.append(cur.val)
                else:
                    level.appendleft(cur.val)

                # If the current node has a left child, enqueue it for future processing
                if cur.left:
                    q.append(cur.left)

                # If the current node has a right child, enqueue it for future processing
                if cur.right:
                    q.append(cur.right)

            # Toggle the flag for the next depth level to reverse the direction
            flag = not flag

            # After processing all nodes at the current depth level, 
            # add the level list to the final result
            res.append(list(level))

        # Return the final zigzag level order traversal result
        return res



        
# @lc code=end

