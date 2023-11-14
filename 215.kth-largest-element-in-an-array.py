#
# @lc app=leetcode id=215 lang=python3
#
# [215] Kth Largest Element in an Array
#

# @lc code=start

import heapq

import heapq  # Importing the heapq module for heap queue algorithm functionalities

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []  # Initialize an empty heap queue (priority queue)
        
        # Loop through each element in the input list 'nums'
        for e in nums:
            # Push the current element 'e' onto the heap. 
            # heapq maintains the heap property (min-heap) where the smallest element is at the root.
            heapq.heappush(pq, e)  
            
            # Check if the size of heap exceeds 'k'
            # If it does, remove the smallest element (root) from the heap.
            # This ensures that the heap always contains 'k' largest elements encountered so far.
            if len(pq) > k:
                heapq.heappop(pq)  
        
        # At the end of the loop, the root of the heap (pq[0]) is the kth largest element.
        # Because we have been maintaining a heap of size 'k' with the k largest elements,
        # the smallest of those elements is the kth largest overall.
        return pq[0]

# @lc code=end

