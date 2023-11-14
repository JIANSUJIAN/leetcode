#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Initiate the tree construction using the provided preorder and inorder lists.
        
        Args:
        - preorder: List[int]: Preorder traversal of the binary tree.
        - inorder: List[int]: Inorder traversal of the binary tree.
        
        Returns:
        - The root node of the constructed binary tree.
        """
        
        # Start the recursive construction process using the entire length of both lists.
        return self.build(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)
    
    def build(self, preorder: List[int], preStart: int, preEnd: int, inorder: List[int], inStart: int, inEnd: int) -> TreeNode:
        """
        Recursive helper function to construct the binary tree using parts of the preorder and inorder lists.
        
        Args:
        - preorder: List[int]: Preorder traversal of the current subtree.
        - preStart: int: Starting index of the current subtree in the preorder list.
        - preEnd: int: Ending index of the current subtree in the preorder list.
        - inorder: List[int]: Inorder traversal of the current subtree.
        - inStart: int: Starting index of the current subtree in the inorder list.
        - inEnd: int: Ending index of the current subtree in the inorder list.
        
        Returns:
        - The root node of the constructed subtree.
        """
        
        # Base case: if the starting index is greater than the ending index in the preorder list, return None.
        if preStart > preEnd:
            return None
        
        # The first element in the current preorder list is the root of the current subtree.
        rootVal = preorder[preStart]
        
        # Find the index of the root value in the inorder list. This will help divide the tree into left and right subtrees.
        index = 0 
        for i in range(inStart, inEnd+1):
            if inorder[i] == rootVal:
                index = i
                break
        
        # Create a new TreeNode with the root value.
        root = TreeNode(rootVal)
        
        # Calculate the size of the left subtree using the index found in the inorder list.
        leftSize = index - inStart
        
        # Recursively construct the left subtree.
        root.left = self.build(preorder, preStart+1, preStart+leftSize,
                               inorder, inStart, index-1)
        
        # Recursively construct the right subtree.
        root.right = self.build(preorder, preStart+leftSize+1, preEnd,
                                inorder, index+1, inEnd)
        
        return root
        
# @lc code=end

