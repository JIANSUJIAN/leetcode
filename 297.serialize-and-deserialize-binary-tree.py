#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# ## 1
# ## Preorder
# class Codec:
#     from collections import deque

#     def __init__(self) -> None:
#         self.SEP = ','
#         self.EMPTY = '#'

#     def serialize(self, root) -> str:
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         sb = []
#         self.serialize_helper(root, sb)
#         return  "".join(sb)
    
#     def serialize_helper(self, root: TreeNode, sb: list):
#         if root is None:
#             sb.append(self.EMPTY)
#             sb.append(self.SEP)
#             return
        
#         sb.append(str(root.val))
#         sb.append(self.SEP)

#         self.serialize_helper(root.left, sb)
#         self.serialize_helper(root.right, sb)


#     def deserialize(self, data: str) -> TreeNode:
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
#         nodes = deque(data.split(self.SEP))
#         return self.deserialize_helper(nodes)
    
#     def deserialize_helper(self, nodes: Deque[str]) -> TreeNode:
#         if not nodes:
#             return None
        
#         first = nodes.popleft()
#         if first == self.EMPTY:
#             return None
        
#         root = TreeNode(int(first))
#         root.left = self.deserialize_helper(nodes)
#         root.right  = self.deserialize_helper(nodes)
#         return root



## 2
## Post order
# class Codec:
#     from collections import deque

#     def __init__(self) -> None:
#         self.SEP = ','
#         self.EMPTY = '#'

#     def serialize(self, root) -> str:
#         """Encodes a tree to a single string.
        
#         :type root: TreeNode
#         :rtype: str
#         """
#         sb = []
#         self.serialize_helper(root, sb)
#         return "".join(sb)
    
#     def serialize_helper(self, root: TreeNode, sb: list):
#         if root is None:
#             sb.append(self.EMPTY)
#             sb.append(self.SEP)
#             return
        
#         # Post-order: Left -> Right -> Root
#         self.serialize_helper(root.left, sb)
#         self.serialize_helper(root.right, sb)
        
#         sb.append(str(root.val))
#         sb.append(self.SEP)

#     def deserialize(self, data: str) -> TreeNode:
#         """Decodes your encoded data to tree.
        
#         :type data: str
#         :rtype: TreeNode
#         """
#         nodes = deque(s for s in data.split(self.SEP) if s)
#         return self.deserialize_helper(nodes)
    
#     def deserialize_helper(self, nodes: Deque[str]) -> TreeNode:
#         if not nodes:
#             return None

#         # Post-order: Last element is the root.
#         last = nodes.pop()
        
#         if last == self.EMPTY:
#             return None

#         root = TreeNode(int(last))
        
#         # Post-order: Left -> Right -> Root
#         root.right = self.deserialize_helper(nodes)  # Right before left due to the stack nature of deque
#         root.left = self.deserialize_helper(nodes)
#         return root


## 3
# class Codec:
#     from collections import deque

#     def __init__(self) -> None:
#         self.SEP = ','
#         self.EMPTY = '#'

#     def serialize(self, root) -> str:
#         if not root:
#             return ""
        
#         sb = []
#         q = deque()
#         q.append(root)

#         while q:
#             cur = q.popleft()
#             if not cur:
#                 sb.append(self.EMPTY)
#                 sb.append(self.SEP)
#                 continue
#             sb.append(str(cur.val))
#             sb.append(self.SEP)

#             q.append(cur.left)
#             q.append(cur.right)
#         return "".join(sb)

#     def deserialize(self, data: str) -> TreeNode:
#         if not data:
#             return None
#         nodes = data.split(self.SEP)[:-1]
#         root = TreeNode(int(nodes[0]))
#         q = deque([root])
#         i = 1
#         while i < len(nodes) and q:
#             node = q.popleft()
#             if nodes[i] != self.EMPTY:
#                 node.left = TreeNode(int(nodes[i]))
#                 q.append(node.left)
#             i += 1
#             if i < len(nodes) and nodes[i] != self.EMPTY:
#                 node.right = TreeNode(int(nodes[i]))
#                 q.append(node.right)
            
#             i += 1
#         return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @lc code=end

