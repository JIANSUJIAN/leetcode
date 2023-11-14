#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if a given tree is a valid Binary Search Tree (BST).

        :param root: Root of the tree.
        :return: True if it's a valid BST, False otherwise.
        """
        return self.isVaildBST_helper(root, None, None)

    def isVaildBST_helper(self, root: TreeNode, min_node: TreeNode, max_node: TreeNode) -> bool:
        """
        Recursively checks the validity of the BST by comparing node values with the given bounds.

        :param root: Current node being checked.
        :param min_node: The node which has the maximum allowable value for the current node.
        :param max_node: The node which has the minimum allowable value for the current node.
        :return: True if the subtree rooted at 'root' is a BST, False otherwise.
        """
        # If current node is None, it's a valid BST
        if not root:
            return True
        
        # If the current node's value is less than or equal to the min_node's value, it's not a BST
        if min_node and root.val <= min_node.val:
            return False
        
        # If the current node's value is greater than or equal to the max_node's value, it's not a BST
        if max_node and root.val >= max_node.val:
            return False
        
        # Check the left subtree with updated maximum bound and 
        # the right subtree with updated minimum bound
        return (self.isVaildBST_helper(root.left, min_node, root) 
                and self.isVaildBST_helper(root.right, root, max_node))

        

        
# @lc code=end

