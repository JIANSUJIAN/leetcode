#
# @lc app=leetcode id=437 lang=python3
#
# [437] Path Sum III
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict

class Solution:
    def __init__(self) -> None:
        # count: Total number of paths found that sum up to the target value.
        self.count = 0
        # k: The target sum.
        self.k = 0
        # h: Default dictionary to store prefix sums and their counts.
        self.h = defaultdict(int)

    def preorder(self, node: TreeNode, curr_sum) -> int:
        """
        Recursive function to traverse the tree in preorder while keeping track of the current path sum.
        
        Parameters:
        - node: Current node in the tree.
        - curr_sum: Accumulated sum from the root to the current node.
        """
        
        # Base case: If node is None, return immediately.
        if not node:
            return
        
        # Update current sum with the node's value.
        curr_sum += node.val

        # If current sum matches target, increment count.
        if curr_sum == self.k:
            self.count += 1
        
        # Increment count by the number of times (curr_sum - k) has been seen before.
        # This indicates that there exists a subarray (path) with sum equal to k.
        self.count += self.h[curr_sum - self.k]

        # Increment the current sum's count in the hash map.
        self.h[curr_sum] += 1

        # Continue traversal in preorder.
        self.preorder(node.left, curr_sum)
        self.preorder(node.right, curr_sum)

        # Backtrack: After exploring both left and right children, decrement the current sum's count.
        # This step ensures that only prefix sums from the current path are considered.
        self.h[curr_sum] -= 1
         
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0 
        self.k = targetSum
        self.preorder(root, 0)
        return self.count

# @lc code=end
