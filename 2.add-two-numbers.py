#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Initialize pointers for both linked lists.
        p1, p2 = l1, l2

        # Create a dummy node as the starting point. The actual result will start from the next node.
        dummy = ListNode(-1)

        # Initialize a current pointer 'p' starting from the dummy node.
        p = dummy
        
        # Initialize 'carry' for values greater than 9.
        carry = 0

        # Continue until you've processed both linked lists and there's no carry left.
        while p1 or p2 or carry:

            # Start with the carry value from the previous operation.
            val = carry

            # If there's a node in l1, add its value and move to the next node.
            if p1: 
                val += p1.val
                p1 = p1.next

            # If there's a node in l2, add its value and move to the next node.
            if p2:
                val += p2.val
                p2 = p2.next
            
            # Compute the new carry and the value for the current position using divmod.
            carry, val = divmod(val, 10)

            # Create a new node with the value and move the current pointer to this new node.
            p.next = ListNode(val)
            p = p.next

        # Return the next node of dummy, which is the start of the result linked list.
        return dummy.next


        
# @lc code=end

