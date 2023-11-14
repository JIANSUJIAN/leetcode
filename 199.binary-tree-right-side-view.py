#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#

# @lc code=start
# Definition for a binary tree node.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        q = []
        q.append(root)
        rightside = []

        while q:
            sz = len(q)

            for i in range(sz):
                cur = q.pop(0)
                if i == sz - 1:
                    rightside.append(cur.val)
                
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)

        return rightside
        


        
# @lc code=end

