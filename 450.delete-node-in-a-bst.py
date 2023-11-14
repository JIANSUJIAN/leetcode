#
# @lc app=leetcode id=450 lang=python3
#
# [450] Delete Node in a BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """
        Deletes a node with the given key in the Binary Search Tree (BST) and 
        returns the new root.

        :param root: The root node of the BST.
        :param key: The key to be deleted.
        :return: The root node of the BST after the deletion.
        """
        
        # If the root is null, simply return None
        if root == None:
            return None
        
        # If the root's value matches the key to be deleted
        if root.val == key:
            
            # If the left child doesn't exist, return the right child 
            # (which can be None or a valid node)
            if root.left == None:
                return root.right
            
            # If the right child doesn't exist, return the left child
            if root.right == None:
                return root.left
            
            # Find the in-order successor (smallest node in root's right subtree)
            minNode = self.getMin(root.right)
            
            # Remove the in-order successor from its original position
            root.right = self.deleteNode(root.right, minNode.val)

            # Assign the entire left subtree of the root to the in-order successor
            minNode.left = root.left
            
            # Assign the entire right subtree of the root (excluding minNode) 
            # to the in-order successor
            minNode.right = root.right
            
            # Replace the root with the in-order successor
            root = minNode
        
        # If the key to be deleted is smaller than the root's value, 
        # then it lies in the left subtree
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        
        # If the key to be deleted is larger than the root's value, 
        # then it lies in the right subtree
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        
        return root
    
    def getMin(self, node: Optional[TreeNode]) ->  Optional[TreeNode]:
        """
        Find the node with the minimum value in the given BST.

        :param node: The root node of the BST.
        :return: The node with the minimum value.
        """
        # Traverse the left side of the BST to find the node with the smallest value
        while node.left != None:
            node = node.left
        return node

        
        

# In the context of the `deleteNode` function, when these lines of code are executed, the objective is to delete the root node (because its value matches the key we want to delete) and replace it with another appropriate node. The typical approach in a BST for this scenario is to replace the node being deleted with either:

# 1. Its in-order predecessor (maximum node value in its left subtree) or
# 2. Its in-order successor (minimum node value in its right subtree).

# In this implementation, the choice is to replace it with the in-order successor, which is the smallest node in its right subtree.

# Here's the detailed breakdown of the code:

# 1. **`minNode.left = root.left`**
   
#    Before this line is executed, `minNode` is the smallest node in the right subtree of `root`. This node doesn't have a left child (because if it had, that child would be smaller and `minNode` wouldn't be the minimum). 
   
#    The line assigns the left child of the current `root` to be the left child of `minNode`. Essentially, we're ensuring that the entire left subtree of the `root` becomes the left subtree of `minNode`.

# 2. **`minNode.right = root.right`**

#    This might look redundant at first since `minNode` is already part of the `root`'s right subtree. But remember, we're going to delete the `root`, and we're also going to delete `minNode` from its original position in the right subtree. 

#    This line ensures that the entire right subtree of the `root` (excluding `minNode`, since it's being moved) becomes the right subtree of `minNode`.

# 3. **`root = minNode`**

#    After rearranging the children of `minNode`, we make `minNode` the new "root" (or parent node for the current sub-tree in consideration). This effectively replaces the original `root` node with `minNode`.

# In essence, this set of operations ensures that the tree remains a valid BST after the node with the desired key (in this case, the root node) is deleted. The choice of `minNode` (the in-order successor) ensures that all BST properties are maintained.



        
# @lc code=end

