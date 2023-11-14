#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 1 Recursive
# class Solution:
#     def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

#         def dfs(node):
#             nonlocal ans
#             if node:
#                 if low <= node.val <= high:
#                     ans += node.val
#                 if low < node.val:
#                     dfs(node.left)
#                 if node.val < high:
#                     dfs(node.right)
#         ans = 0
#         dfs(root)
#         return ans



# 2 Iterative        
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    ans += node.val
                if low < node.val:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        return ans
        
# @lc code=end

