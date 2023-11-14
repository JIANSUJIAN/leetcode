#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def findFromdEnd(self, head: ListNode, k: int) -> ListNode:
        # Initialize p1 and move it k steps ahead
        p1 = head
        for i in range(k):
            if not p1:
                return None
            p1 = p1.next
        
        # Initialize p2 at the head
        p2 = head
        # Move both pointers until p1 reaches the end
        while p1:
            p1 = p1.next
            p2 = p2.next
        
        # p2 now points to the kth node from the end
        return p2

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Initialize a dummy node before the head to handle edge cases
        dummy = ListNode(-1)
        dummy.next = head
        
        # Find the (n+1)th node from the end, which is the node just before the one to be deleted
        x = self.findFromdEnd(dummy, n + 1)
        
        # If x or x.next is None, it means the list has less than n nodes
        if x and x.next:
            x.next = x.next.next
        
        # Return the next of dummy, which is the new head of the list
        return dummy.next

        
# @lc code=end

