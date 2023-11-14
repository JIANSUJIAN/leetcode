#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers, slow and fast, to traverse the list.
        slow, fast = head, head 

        # Move the fast pointer at double the speed of the slow pointer.
        # When fast reaches the end, slow will be at the midpoint.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # If there's an odd number of elements, move the slow pointer one step further.
        if fast:
            slow = slow.next

        # Reverse the second half of the list starting from the slow pointer.
        right = self.reverse(slow)

        # Initialize the left pointer to start of the list.
        left = head

        # Compare values from the original and reversed half.
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        # If all values matched, the linked list is a palindrome.
        return True
    
    def reverse(self, head: ListNode) -> ListNode:
        # Initialize previous pointer to None and current pointer to the head of the list.
        pre, cur = None, head
        
        # Traverse the list while reversing the links.
        while cur:
            next_node = cur.next  # temporarily store the next node
            cur.next = pre        # reverse the current node's link
            pre = cur             # move the previous pointer to current node
            cur = next_node       # move to the next node

        # Return the new head of the reversed list.
        return pre

        


        
# @lc code=end

