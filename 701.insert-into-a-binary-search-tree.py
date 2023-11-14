#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Inserts a new node with the given value into a Binary Search Tree (BST).

        :param root: The root node of the BST.
        :param val: The value to insert into the BST.
        :return: The root node of the BST after the insertion.
        """
        
        # If the tree is empty, create a new node with the given value and return it
        if not root:
            return TreeNode(val)
        
        # If the value to insert is greater than the current node's value, 
        # insert it in the right subtree
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        
        # If the value to insert is less than the current node's value, 
        # insert it in the left subtree
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        
        # Return the (potentially modified) current node
        return root
        
        
# @lc code=end

