#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Initialize pointers l and r at the root.
        l = root 
        r = root
        # hl will store the height of the left subtree, and hr the height of the right subtree.
        hl = 0
        hr = 0
        
        # Traverse the leftmost path of the tree to compute its height (hl).
        while l is not None:
            l = l.left
            hl += 1
        
        # Traverse the rightmost path of the tree to compute its height (hr).
        while r is not None:
            r = r.right
            hr += 1
        
        # If the height of the left and right subtrees are equal, the tree is full.
        # Therefore, the number of nodes is 2^hl - 1.
        if hl == hr:
            return pow(2, hl) - 1
        
        # If the tree isn't full, recursively compute the number of nodes in the left and right subtrees.
        # Add 1 for the root node.
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


# The function `countNodes` attempts to determine the number of nodes in a complete binary tree. The methodology used is to check if the tree is a perfect binary tree (where the left and right subtree heights are the same) or if it's just complete.

# 1. **Finding the height of the tree**:
#     - The code first calculates the height of the tree using the leftmost and rightmost paths. This is done by traversing down the left and right sides of the tree.
#     - For a balanced binary tree, this takes \(O(\log n)\) time for the left side and \(O(\log n)\) time for the right side.
#     - So, combined, the time taken for height calculation is \(2 \times O(\log n) = O(\log n)\).

# 2. **Recursive Decomposition**:
#     - If the tree is found to be perfect (where left and right subtree heights are the same), the total number of nodes is calculated directly using \(2^{\text{height}} - 1\). This takes constant time, i.e., \(O(1)\).
#     - If the tree is not perfect, then the function dives deeper into both left and right subtrees. The key observation here is that at each recursive call, one of the two subtrees will be a perfect binary tree (because the tree is complete but not perfect). Thus, we don't have to make two recursive calls at each level.
#     - This means that, in the worst case, the function will make a recursive call down each level of the tree, which is \(O(\log n)\) levels deep.
#     - In each of these recursive calls, the height calculation is made again, costing another \(O(\log n)\).
#     - This results in \(O(\log n) \times O(\log n) = O((\log n)^2)\) for the recursive decomposition.

# Combining both the height calculation and the recursive decomposition, the total time complexity of the function is \(O((\log n)^2)\).
        
# @lc code=end

