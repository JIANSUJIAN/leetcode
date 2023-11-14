#
# @lc app=leetcode id=382 lang=python3
#
# [382] Linked List Random Node
#

# @lc code=start
# Definition for singly-linked list.

import random

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        
    def getRandom(self) -> int:

        chosen = 0
        scope = 1
        curr = self.head

        while curr:
            if random.random() < 1 / scope:
                chosen = curr.val
            curr = curr.next
            scope += 1
        
        return chosen
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
# @lc code=end

