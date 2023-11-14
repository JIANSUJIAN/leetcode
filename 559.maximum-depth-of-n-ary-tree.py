#
# @lc app=leetcode id=559 lang=python3
#
# [559] Maximum Depth of N-ary Tree
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

## 1. Divide 
# class Solution:
#     def maxDepth(self, root: 'Node') -> int:
#         if not root:
#             return 0
        
#         subTreeMaxDepth = 0
#         for child in root.children:
#             subTreeMaxDepth = max(subTreeMaxDepth, self.maxDepth(child))
#         return 1 + subTreeMaxDepth

## 2. traverse
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        self.traverse(root)
        return self.res
      
    def __init__(self) -> None:
        self.depth = 0
        self.res = 0

    def traverse(self, root) -> None:
        if not root:
            return 

        self.depth += 1
        self.res = max(self.res, self.depth)

        for child in root.children:
            self.traverse(child)
        self.depth -= 1
        
# @lc code=end

