#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Recursive
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     # Base case: If the list is empty or contains only one node, 
    #     # it's already reversed.
    #     if head is None or head.next is None:
    #         return head

    #     # Recursive call: Reverse everything from the second node onward.
    #     # 'last' will eventually be the last node in the list (and will 
    #     # become the new head of the reversed list).
    #     last = self.reverseList(head.next)

    #     # At this point, 'last' is the last node in the original list.
    #     # We adjust the next node's 'next' pointer to point back to the current node.
    #     # This essentially reverses the link direction between the current node 
    #     # and the next node.
    #     head.next.next = head

    #     # After reversing the link direction, set current node's 'next' to None
    #     # to remove its forward link. This ensures it doesn't create a cycle.
    #     head.next = None

    #     # Return the new head of the reversed segment. It remains constant 
    #     # through all the recursive calls.
    #     return last

        
    # 2. Iterative
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize the previous node to None. This will be the new tail after reversing.
        prev = None
        
        # Start with the head of the list as the current node.
        curr = head
    
        # Iterate until we have processed all nodes in the list.
        while curr:
            # Save the next node so we can continue the traversal.
            next_temp = curr.next
            
            # Reverse the 'next' pointer of the current node.
            curr.next = prev
            
            # Move the 'prev' and 'curr' pointers one step forward.
            prev = curr
            curr = next_temp
    
        # At the end, 'prev' will point to the new head (previously the tail) of the reversed list.
        return prev
    
    
        
# @lc code=end

