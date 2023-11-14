#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: if the list is empty, return None.
        if not head:
            return None
        
        # 'slow' pointer points to the last known unique node.
        # 'fast' pointer is used to scan through the linked list.
        slow, fast = head, head

        # Continue until 'fast' has traversed all nodes.
        while fast:
            # If the current node (pointed by 'fast') has a different value from the last unique node (pointed by 'slow')...
            if fast.val != slow.val:
                # Make the next node of 'slow' as the current unique node ('fast').
                slow.next = fast
                # Move 'slow' to its next node.
                slow = slow.next

            # Move 'fast' to its next node to continue scanning.
            fast = fast.next

        # After the loop, the 'slow' pointer will point to the last unique node.
        # So, we should set its next node to None to ensure the correct termination of the modified linked list.
        slow.next = None

        # Return the modified head of the list.
        return head

        
# @lc code=end

