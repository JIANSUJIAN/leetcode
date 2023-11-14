#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode):
        # Initialize an empty stack to store nodes for in-order traversal.
        self.stack = []
        # Pointer pointing to the current node, starting at the root.
        self.curr = root

    def hasNext(self) -> bool:
        # Return True if there are still unvisited nodes in the BST.
        # Either there are nodes stored in the stack or the current node is not None.
        return self.curr is not None or bool(self.stack)

    def next(self) -> int:
        # The goal is to return the next smallest element in the BST.
        
        # Push all the left children of the current node onto the stack.
        # This ensures we process the left child before the current node,
        # adhering to the in-order traversal's left -> current -> right sequence.
        while self.curr:
            self.stack.append(self.curr)
            self.curr = self.curr.left
        
        # Pop the node at the top of the stack, which is the next node
        # in the in-order sequence (i.e., the next smallest unvisited node).
        node = self.stack.pop()
        
        # Set the current node to the right child of the popped node.
        # This ensures that after processing the current node, the next node
        # in the in-order sequence is its right child (if it exists).
        self.curr = node.right
        
        # Return the value of the popped node.
        return node.val

        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

