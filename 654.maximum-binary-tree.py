#
# @lc app=leetcode id=654 lang=python3
#
# [654] Maximum Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        """
        Public method to initiate the construction of a maximum binary tree.
        
        Args:
        - nums: List of integers from which the binary tree will be constructed.

        Returns:
        - The root node of the constructed maximum binary tree.
        """
        
        return self.build(nums, 0, len(nums) - 1)
    
    def build(self, nums: List[int], lo: int, hi: int) -> TreeNode:
        """
        Recursive helper method to construct the maximum binary tree from a sublist of nums.

        Args:
        - nums: List of integers from which the binary tree will be constructed.
        - lo: The starting index of the sublist from which the current binary tree will be constructed.
        - hi: The ending index of the sublist from which the current binary tree will be constructed.

        Returns:
        - The root node of the constructed maximum binary tree for the given sublist.
        """
        
        # Base case: if the starting index is greater than the ending index, return None.
        if lo > hi:
            return None
        
        # Initialize variables to keep track of the index and value of the maximum element in the sublist.
        index, maxVal = -1, -sys.maxsize
        
        # Iterate over the sublist and find the maximum element and its index.
        for i in range(lo, hi+1):
            if maxVal < nums[i]:
                index = i
                maxVal = nums[i]
        
        # Create a new TreeNode with the maximum value.
        root = TreeNode(maxVal)
        
        # Recursively construct the left subtree from the elements before the maximum element in the sublist.
        root.left = self.build(nums, lo, index - 1)
        
        # Recursively construct the right subtree from the elements after the maximum element in the sublist.
        root.right = self.build(nums, index + 1, hi)
        
        return root
        
# @lc code=end

