#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a sentinel node, which acts as a preceding node to the head.
        sentinel = ListNode(0, head)
        # The predecessor variable 'pred' is used to link nodes and skip duplicates.
        pred = sentinel

        # Traverse the linked list.
        while head:
            # If the current node has a duplicate value with the next node.
            if head.next and head.val == head.next.val:
                # Skip all the nodes with the same value.
                while head.next and head.val == head.next.val:
                    head = head.next
                # Point the predecessor's next to the next distinct value.
                pred.next = head.next
            else:
                # If the current node is not a duplicate, move the predecessor to the current node.
                pred = pred.next

            # Move to the next node in the list.
            head = head.next

        # Return the start of the cleaned-up list.
        return sentinel.next


        
# @lc code=end

