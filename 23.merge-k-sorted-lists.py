#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Initialize a dummy node to serve as the start of the merged list.
        dummy = ListNode(-1)
        
        # 'p' is a moving pointer, starting at the dummy node, that'll help in building the merged list.
        p = dummy
        
        # The heap 'h' will be used to keep track of the smallest node among all the lists.
        h = []

        # Iterate through each list and push the head node (if it exists) to the heap.
        for i in range(len(lists)):
            if lists[i]:
                # Push the tuple (node value, list index) into the heap.
                heapq.heappush(h, (lists[i].val, i))
                
                # Move to the next node in the current list.
                lists[i] = lists[i].next

        # Continue until all nodes from all lists have been processed.
        while h:
            # Pop the smallest value and its corresponding list index from the heap.
            val, i = heapq.heappop(h)
            
            # Create a new node with the smallest value and attach it to the merged list.
            p.next = ListNode(val)
            
            # Move the pointer 'p' forward.
            p = p.next

            # If the list from which we just extracted a node still has more nodes left...
            if lists[i]:
                # Push the next node's value (lists[i].val) from the same list into the heap. 
                # We also push 'i' which serves as an identifier for the list so that we know 
                # from which list this node was taken. This way, we ensure that the heap always 
                # contains the current smallest nodes from the front of each of the 'k' lists.
                heapq.heappush(h, (lists[i].val, i))
        
                # Move the pointer of list 'i' to its next node. This is because we have now 
                # processed the current node (by pushing it to the heap) and should consider 
                # its next node in future iterations. If we didn't advance this pointer, we'd 
                # be repeatedly pushing the same node into the heap, which is incorrect.
                lists[i] = lists[i].next
        

        # Return the merged list, starting from the next of dummy.
        return dummy.next




        
# @lc code=end

