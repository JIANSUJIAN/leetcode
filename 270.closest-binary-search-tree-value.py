#
# @lc app=leetcode id=270 lang=python3
#
# [270] Closest Binary Search Tree Value
#

# @lc code=start


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Approach 1: Linear Time
# Time: O(N) Space: O(N)
# class Solution:
#     def closestValue(self, root: Optional[TreeNode], target: float) -> int:

#         def inorder(r: TreeNode):
#             return inorder(r.left) + [r.val] + inorder(r.right) if r else []
        
#         return min(inorder(root), key = lambda x: abs(target - x))
        
# Approach 2: Iterative Inorder
# Time: O(H + k) Space: O(H)


# class Solution:
#     def closestValue(self, root: Optional[TreeNode], target: float) -> int:
#         stack = []
#         closest = float('inf')

#         # Continue traversal as long as there are nodes to process
#         while stack or root:  # stack: nodes to backtrack to, root: current node
#             # Traverse to the leftmost node
#             while root:
#                 stack.append(root)  # Push current node to stack before going left
#                 root = root.left

#             root = stack.pop()  # Backtrack to the last visited node

#             # Update closest value if necessary
#             if abs(target - closest) > abs(target - root.val):
#                 closest = root.val

#             # If current value is greater than target, no need to go further
#             if root.val > target:
#                 break
            
#             root = root.right  # Move to the right subtree

#         return closest


# Approach 3: Binary Search
# Time: O(H)  Space: O(1)
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        closest = root.val
        while root:
            closest = min(root.val, closest, key=lambda x: (abs(target - x), x))

            if target < root.val:
                root = root.left
            else:
                root = root.right
        return closest







        
# @lc code=end

