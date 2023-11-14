#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        Definition for a binary tree node.
        
        Attributes:
        - val: Value of the node.
        - left: Left child node.
        - right: Right child node.
        """
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self) -> None:
        """
        Initialize the Solution object with:
        - a dictionary to store serialized subtrees and their occurrence frequencies.
        - a list to store results (root nodes of duplicate subtrees).
        """
        self.subTrees = {}
        self.res = []

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        """
        Find and return all root nodes of duplicate subtrees.
        
        Args:
        - root: Root node of the binary tree.
        
        Returns:
        - List of root nodes of duplicate subtrees.
        """
        self.serialize(root)
        return self.res

    def serialize(self, root: TreeNode) -> str:
        """
        Recursive function to serialize a subtree rooted at `root`.
        
        Args:
        - root: Root node of the subtree.
        
        Returns:
        - Serialized representation of the subtree rooted at `root`.
        """
        
        # Base case: if the current node is null, return "#" as a placeholder.
        if not root:
            return "#"

        # Serialize the left and right subtrees.
        left = self.serialize(root.left)
        right = self.serialize(root.right)

        # Create a unique serialized representation for the current subtree.
        # The representation is a combination of serialized left and right subtrees, and the value of the current node.
        myself = left + "," + right + "," + str(root.val)

        # Check how many times the current serialized subtree has appeared before.
        freq = self.subTrees.get(myself, 0)
        
        # If the subtree has appeared exactly once before, add it to the result list.
        # We only add it once to avoid duplicates in the result.
        if freq == 1:
            self.res.append(root)
        
        # Update the frequency count of the current serialized subtree.
        self.subTrees[myself] = freq + 1
        
        return myself


        
# @lc code=end

