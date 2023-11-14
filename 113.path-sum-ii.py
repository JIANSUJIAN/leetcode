#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def recurseTree(self, node, remainingSum, pathNodes, pathList):
        """
        Recursive helper function to traverse the tree and find paths that sum up to the target.
        
        Parameters:
        - node: Current node in the tree.
        - remainingSum: The remaining sum to be achieved from the current node to a leaf.
        - pathNodes: List storing the current path being considered.
        - pathList: List storing all the valid paths.
        """
        
        # Base case: If node is None, return immediately.
        if not node:
            return None

        # Add the current node's value to the current path.
        pathNodes.append(node.val)

        # If current node is a leaf and its value equals the remaining sum, 
        # it means we found a valid path.
        if remainingSum == node.val and not node.left and not node.right:      
            pathList.append(list(pathNodes))
        else:
            # Continue the search on left and right child.
            self.recurseTree(node.left, remainingSum - node.val, pathNodes, pathList)
            self.recurseTree(node.right, remainingSum - node.val, pathNodes, pathList)

        # Backtrack: Remove the current node's value from the current path. This step
        # effectively takes the function one step back up the tree, allowing it to explore 
        # other branches. Think of it as "undoing" the last choice made in the current path,
        # enabling the algorithm to explore other potential solutions in a depth-first manner.
        pathNodes.pop()

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        Initiates the recursive search for paths in the tree that sum up to the target value.
        
        Parameters:
        - root: Root node of the tree.
        - targetSum: Target sum that each path should achieve.
        
        Returns:
        - List of lists where each inner list represents a valid path.
        """
        pathList = []
        self.recurseTree(root, targetSum, [], pathList)
        return pathList

# @lc code=end

