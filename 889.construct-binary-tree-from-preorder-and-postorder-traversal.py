#
# @lc app=leetcode id=889 lang=python3
#
# [889] Construct Binary Tree from Preorder and Postorder Traversal
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
        Initialize the Solution object with a dictionary to keep track of 
        the indices of values in the postorder traversal.
        """
        self.valToIndex = {}

    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        Construct a binary tree from its preorder and postorder traversal lists.
        
        Args:
        - preorder: List[int]: Preorder traversal of the binary tree.
        - postorder: List[int]: Postorder traversal of the binary tree.
        
        Returns:
        - The root node of the constructed binary tree.
        """

        # Populate the valToIndex dictionary with indices of values from the postorder traversal.
        for i in range(len(postorder)):
            self.valToIndex[postorder[i]] = i

        # Start the recursive tree construction using the entire length of both lists.
        return self.build(preorder, 0, len(preorder)-1,
                          postorder, 0, len(postorder)-1)
        
    def build(self, preorder: List[int], preStart: int, preEnd: int,
              postorder: List[int], postStart: int, postEnd: int) -> TreeNode:
        """
        Recursive helper function to construct the binary tree using parts of the preorder and postorder lists.
        
        Args:
        - preorder: List[int]: Preorder traversal of the current subtree.
        - preStart, preEnd: Define the segment of the preorder list to consider for the current subtree.
        - postorder: List[int]: Postorder traversal of the current subtree.
        - postStart, postEnd: Define the segment of the postorder list to consider for the current subtree.
        
        Returns:
        - The root node of the constructed subtree.
        """

        # Base case: if the current segment of the preorder list is empty, return None.
        if preStart > preEnd:
            return None
        
        # Base case: if only one element is left in the segment, create and return a node.
        if preStart == preEnd:
            return TreeNode(preorder[preStart])

        # The first element in the current preorder list is the root of the current subtree.
        rootVal = preorder[preStart]
        
        # The second element in the current preorder list is the root of the left subtree.
        leftRootVal = preorder[preStart+1]

        # Find the index of the root of the left subtree in the postorder list.
        index = self.valToIndex[leftRootVal]
        
        # Calculate the size of the left subtree using its end index in the postorder list.
        leftSize = index - postStart + 1

        # Create a new TreeNode with the root value.
        root = TreeNode(rootVal)

        # Recursively construct the left subtree.
        root.left = self.build(preorder, preStart+1, preStart+leftSize,
                               postorder, postStart, index)

        # Recursively construct the right subtree.
        root.right = self.build(preorder, preStart+leftSize+1, preEnd,
                                postorder, index+1, postEnd-1)

        return root
        
# @lc code=end

