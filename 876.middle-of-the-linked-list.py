#
# @lc app=leetcode id=876 lang=python3
#
# [876] Middle of the Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize two pointers: 'slow' will move one step at a time, while 'fast' will move two steps.
        slow = head
        fast = head
        
        # Loop until 'fast' pointer reaches the end of the list.
        while fast and fast.next:
            # Move the 'slow' pointer one step.
            slow = slow.next
            
            # Move the 'fast' pointer two steps.
            fast = fast.next.next
        
        # When 'fast' reaches the end of the list, 'slow' will be at the middle.
        # Return the 'slow' pointer which now points to the middle node.
        return slow

        
# @lc code=end

