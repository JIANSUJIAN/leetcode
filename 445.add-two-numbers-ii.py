#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1. reverse then add two numbers as in problem [2]
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

#         l1 = self.reverse(l1)
#         l2 = self.reverse(l2)

#         p1, p2 = l1, l2
#         dummy = ListNode(-1)
#         p = dummy

#         carry = 0

#         while p1 or p2 or carry:
            
#             val = carry

#             if p1:
#                 val += p1.val
#                 p1 = p1.next
            
#             if p2:
#                 val += p2.val
#                 p2 = p2.next
            
#             carry, val = divmod(val, 10)

#             p.next =ListNode(val)
#             p = p.next

#         return self.reverse(dummy.next)


#     def reverse(self, head: ListNode) -> ListNode:
#         pre, cur = None, head

#         while cur:
#             next_node = cur.next
#             cur.next = pre
#             pre = cur
#             cur = next_node
        
#         return pre

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        stk1 = []
        while l1:
            stk1.append(l1.val)
            l1 = l1.next
        stk2 = []
        while l2:
            stk2.append(l2.val)
            l2 = l2.next
        
        dummy = ListNode(-1)
        carry = 0

        while stk1 or stk2 or carry > 0:

            val = carry
            if stk1:
                val += stk1.pop()
            if stk2:
                val += stk2.pop()
            
            carry, val = divmod(val, 10)

            newNode = ListNode(val)
            newNode.next = dummy.next
            dummy.next = newNode
        return dummy.next
   
# @lc code=end

