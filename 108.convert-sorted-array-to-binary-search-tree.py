#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def construct(self, nums, left: int, right: int) -> TreeNode:
        # Base condition: if left pointer surpasses right pointer, 
        # it means this subarray doesn't have elements to construct a subtree.
        if left > right:
            return None
        
        # Choose the middle element to be the root of this subtree. 
        # This ensures the resulting tree is height-balanced.
        p = (left + right) // 2

        # Create a new tree node with the middle element.
        root = TreeNode(nums[p])

        # Recursively construct the left subtree using elements before the middle element.
        root.left = self.construct(nums, left, p - 1)

        # Recursively construct the right subtree using elements after the middle element.
        root.right = self.construct(nums, p + 1, right)
        
        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Start the construction using the whole array.
        # This function serves as the starting point for the recursive construction.
        return self.construct(nums, 0, len(nums) -1)

        
# @lc code=end

