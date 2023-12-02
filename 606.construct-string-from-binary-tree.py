#
# @lc app=leetcode id=606 lang=python3
#
# [606] Construct String from Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Approach 1: Recursion

# class Solution:
#     def tree2str(self, root: Optional[TreeNode]) -> str:
#         res = []
#         self.dfs(root, res)
#         return ''.join(res)

#     def dfs(self, root, res):
#         if not root:
#             return
        
#         res.append(str(root.val))

#         if not root.left and not root.right:
#             return
#         res.append('(')
#         self.dfs(root.left, res)
#         res.append(')')
#         if root.right:
#             res.append('(')
#             self.dfs(root.right, res)
#             res.append(')')

# Approach 2: Iterative Method Using stack

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        
        stack = [root]
        visited = set()
        res = []

        while stack:
            root = stack[-1]
            if root in visited:
                stack.pop()
                res.append(')')
            else:
                visited.add(root)
                res.append('(' + str(root.val))
                if not root.left and root.right:
                    res.append('()') 
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        return ''.join(res)[1:-1]



        
# @lc code=end

