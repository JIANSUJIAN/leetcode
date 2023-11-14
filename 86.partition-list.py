#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        # Initial dummy nodes to assist with building the two resultant lists.
        dummy1 = ListNode(-1)  # To store values < x 
        dummy2 = ListNode(-1)  # To store values >= x

        p1, p2 = dummy1, dummy2
        p = head

        while p:
            # If current node's value is greater than or equal to 'x', append to second list.
            if p.val >= x:
                p2.next = p
                p2 = p2.next
            # Otherwise, append to the first list.
            else:
                p1.next= p
                p1 = p1.next
            
            # Detach the current node from the original list.
            # We save the next node first, then set p.next to None 
            # to break the link. Then we move 'p' to the saved next node.
            # This approach ensures we do not lose the reference to the next node 
            # in the original list after appending current node to one of the new lists.
            temp = p.next
            p.next = None
            p = temp

        # Link the end of the first list (values < x) to the start of the second list (values >= x).
        p1.next = dummy2.next
    
        return dummy1.next



        
        
# @lc code=end

