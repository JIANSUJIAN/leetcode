#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Search for a node with the given value in a Binary Search Tree (BST).

        :param root: The root node of the BST.
        :param val: The value to search for.
        :return: The node with the given value if found, otherwise None.
        """
        
        # If the current node is None, the value is not in the tree
        if not root:
            return None
        
        # If the current node's value is greater than the target value, 
        # search in the left subtree
        if root.val > val:
            return self.searchBST(root.left, val)
        
        # If the current node's value is less than the target value, 
        # search in the right subtree
        if root.val < val:
            return self.searchBST(root.right, val)
        
        # If the current node's value matches the target value, return the node
        return root
        


        
# @lc code=end

