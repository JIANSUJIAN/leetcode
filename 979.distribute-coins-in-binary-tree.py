#
# @lc app=leetcode id=979 lang=python3
#
# [979] Distribute Coins in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def distributeCoins(self, root):
        # Initialize the number of moves to zero
        self.moves= 0

        def dfs(node):
            """
            Perform a depth-first traversal of the tree to calculate and balance the coins.
            
            :param node: Current tree node being processed
            :return: Coin balance for the current node
            """
            # Base case: If node is None, it contributes no coins
            if not node: 
                return 0
            
            # Recursively get the coin balance for the left and right children
            L, R = dfs(node.left), dfs(node.right)
            
            # The number of moves is the sum of the absolute values of coins needed
            # to balance the left and right children
            self.ans += abs(L) + abs(R)
            
            # Return the overall coin balance for this node (after ensuring this node has 1 coin)
            # Positive values indicate excess coins; negative values indicate a coin deficit
            return node.val + L + R - 1

        # Start the DFS traversal from the root node
        dfs(root)
        
        # Return the total number of moves needed to balance the entire tree
        return self.moves

        
# @lc code=end

