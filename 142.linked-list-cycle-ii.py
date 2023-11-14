#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Initialize two pointers: 'slow' will move one step at a time, while 'fast' will move two steps.
        fast, slow = head, head
        
        # This flag is used to determine if a cycle was found.
        cycle_detected = False

        # Check if the list has a cycle.
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                cycle_detected = True
                break
        
        # If no cycle was detected, return None.
        if not cycle_detected:
            return None
        
        # Reset slow to the head. The distance between the head and the start of the cycle is equal 
        # to the distance between the meeting point inside the cycle and the start of the cycle.
        slow = head

        # Move both pointers one step at a time until they meet again, which will be the start of the cycle.
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        # Return the node where the cycle starts.
        return slow 

# @lc code=end

