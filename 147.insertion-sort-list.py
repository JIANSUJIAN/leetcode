#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Base case: If list is empty or contains only one node, return it.
        if not head or not head.next:
            return head

        # Initialize dummy node for the result list to simplify insertion.
        dummy =  ListNode(-1, head)

        # 'last_sorted' points to the last node in the sorted part.
        last_sorted = head

        # 'cur' starts from the second node to be inserted into the sorted list.
        cur = head.next

        while cur:
            # If current node is greater than or equal to the last sorted node,
            # it's already in its correct position.
            if cur.val >= last_sorted.val:
                last_sorted = last_sorted.next
            else:
                # Else, find the correct position to insert 'cur' in the sorted list.
                prev = dummy
                while prev.next.val <= cur.val:
                    prev = prev.next

                # Adjust pointers to insert 'cur'.
                last_sorted.next = cur.next
                cur.next = prev.next
                prev.next = cur
            
            # Move to the next node in the original list.
            cur = last_sorted.next

        # Return the sorted list starting from the node after dummy.
        return dummy.next


        
# @lc code=end

