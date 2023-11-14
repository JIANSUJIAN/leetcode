#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to act as the starting point of the merged list.
        dummy = ListNode(-1)
        
        # `p` is a pointer that will move through the new merged list.
        p = dummy
        
        # `p1` and `p2` are pointers for list1 and list2, respectively.
        p1 = list1
        p2 = list2

        # Traverse through the lists as long as there are elements in both.
        while p1 and p2:
            # Compare the current values of p1 and p2.
            if p1.val > p2.val:
                # If p2's value is smaller, append it to the merged list.
                p.next = p2 
                # Move p2 to its next node.
                p2 = p2.next
            else:
                # If p1's value is smaller or equal, append it to the merged list.
                p.next = p1
                # Move p1 to its next node.
                p1 = p1.next
            # Move to the next position in the merged list.
            p = p.next

        # If there are remaining elements in p1, append them.
        if p1:
            p.next = p1
        
        # If there are remaining elements in p2, append them.
        if p2:
            p.next = p2

        # Return the merged list starting from the node after dummy.
        return dummy.next





        
# @lc code=end

