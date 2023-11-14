#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        """
        A basic definition for a binary tree node.
        
        Attributes:
        - val: Value of the node.
        - left: Left child node.
        - right: Right child node.
        """
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Construct a binary tree from its inorder and postorder traversal lists.
        
        Args:
        - inorder: List[int]: Inorder traversal of the binary tree.
        - postorder: List[int]: Postorder traversal of the binary tree.
        
        Returns:
        - The root node of the constructed binary tree.
        """
        
        # Create a dictionary to quickly look up the index of an element in the inorder list.
        valToIndex = {}
        for i in range(len(inorder)):
            valToIndex[inorder[i]] = i
        
        # Start the recursive tree construction process using the entire length of both lists.
        return self.build(inorder, 0, len(inorder)-1,
                          postorder, 0, len(postorder)-1, valToIndex)
    
    def build(self, inorder: List[int], inStart: int, inEnd: int,
              postorder: List[int], postStart: int, postEnd: int,
              valToIndex: dict) -> TreeNode:
        """
        Recursive helper function to construct the binary tree using parts of the inorder and postorder lists.
        
        Args:
        - inorder: List[int]: Inorder traversal of the current subtree.
        - inStart, inEnd: Define the segment of the inorder list to consider for the current subtree.
        - postorder: List[int]: Postorder traversal of the current subtree.
        - postStart, postEnd: Define the segment of the postorder list to consider for the current subtree.
        - valToIndex: dict: A lookup table to get the index of a value in the inorder list.
        
        Returns:
        - The root node of the constructed subtree.
        """
        
        # Base case: if the current segment of the inorder list is empty, return None.
        if inStart > inEnd:
            return None
        
        # The last element in the current postorder list is the root of the current subtree.
        rootVal = postorder[postEnd]
        
        # Retrieve the index of the root value in the inorder list using the lookup table.
        index = valToIndex[rootVal]
        
        # Create a new TreeNode with the root value.
        root = TreeNode(rootVal)
        
        # Calculate the size of the left subtree using the index found in the inorder list.
        leftSize = index - inStart
        
        # Recursively construct the left subtree. 
        # Note the `-1` in `postStart+leftSize-1`. It's to ensure we're selecting the correct segment of the postorder list.
        root.left = self.build(inorder, inStart, index-1,
                               postorder, postStart, postStart+leftSize-1, valToIndex)
        
        # Recursively construct the right subtree.
        root.right = self.build(inorder, index+1, inEnd,
                                postorder, postStart+leftSize, postEnd-1, valToIndex)
        
        return root
        
# @lc code=end

