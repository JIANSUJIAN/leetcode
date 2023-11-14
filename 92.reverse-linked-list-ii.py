#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1 Recursive
# class Solution:
#     def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
#         """
#         Reverse the nodes of the list from position 'left' to position 'right'.
#         If 'left' is 1, it means we start reversing from the head itself.
#         """
        
#         # If we are starting to reverse from the very first node
#         if left == 1:
#             return self.reverseN(head, right)
        
#         # Recursive case: Move to the next node while decrementing 'left' and 'right'.
#         # This is done to find the exact segment of the list that needs to be reversed.
#         head.next = self.reverseBetween(head.next, left - 1, right -1)
        
#         # Return the head, as outside of the segment to reverse, the list remains unchanged.
#         return head

#     def reverseN(self, head: ListNode, n: int) -> ListNode:
#         """
#         Reverse the first 'n' nodes in the linked list.
#         """
        
#         # Base case: if n is 1, it indicates the point up to which nodes should be reversed.
#         if n == 1:
#             # Keep track of the node immediately after the segment to be reversed.
#             # This ensures we connect the reversed segment correctly to the rest of the list.
#             self.successor = head.next
#             return head
        
#         # Recursively reverse the next 'n-1' nodes.
#         last = self.reverseN(head.next, n - 1)

#         # Perform the reversal: the next node's 'next' points back to the current head.
#         head.next.next = head

#         # The current head's next should point to the 'successor' after the segment is reversed.
#         head.next = self.successor
        
#         # Return the 'last' node, which is now the new head of the reversed segment.
#         return last



# 2. Iterative
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        cur, prev = head, None
        # Move `cur` to the starting position of the segment to be reversed.
        # Meanwhile, `prev` will point to the node right before the start of the segment.
        while left > 1:
            prev = cur
            cur = cur.next
            left, right = left - 1, right - 1
        
        # After the above traversal:
        # `tail` will be the starting node of the segment to be reversed.
        # `con` will be the node immediately preceding the segment to be reversed. 
        # If the segment starts from the head, `con` will be None.
        tail, con = cur, prev

        # Standard linked list reversal code.
        # Keep reversing the links for nodes within the segment.
        while right:
            next_temp = cur.next
            cur.next = prev
            prev = cur
            cur = next_temp
            right -= 1
        
        # Connect the end of the reversed segment back to the remaining list.
        tail.next = cur

        # If there was a node before the reversed segment (`con` is not None), 
        # connect it to the start of the reversed segment.
        if con:
            con.next = prev
        else:
            # If the reversed segment started from the head, update the head of the list.
            head = prev
            
        return head





        


        
# @lc code=end

