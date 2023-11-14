#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        # Variable to store the kth smallest element
        self.res = 0
        # Variable to keep track of the rank/position of the current node 
        # during the in-order traversal
        self.rank = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Returns the kth smallest element in a BST.

        :param root: Root of the BST.
        :param k: The rank of the required smallest element.
        :return: The kth smallest element in the BST.
        """
        self.traverse(root, k)
        return self.res
    
    def traverse(self, root: TreeNode, k: int) -> None:
        """
        Helper function to perform in-order traversal on the BST.

        During the traversal, it updates the rank of each node. 
        When the rank matches the required k, it updates the result.

        :param root: Current root during traversal.
        :param k: The rank of the required smallest element.
        """
        if not root:
            return
        
        # Traverse the left subtree
        self.traverse(root.left, k)

        # Increase the rank as we visit the node in in-order manner
        self.rank += 1

        # Check if current node's rank matches the required k
        if k == self.rank:
            self.res = root.val
            return

        # Traverse the right subtree
        self.traverse(root.right, k)

# @lc code=end

