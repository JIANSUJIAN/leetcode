#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#

# @lc code=start
# Approach 1: Min-Heap approach

import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        # size of the n x n matrix
        n = len(matrix)

        # initialize the min-heap. Instead of pushing all elements into the heap
        # we'll only push the first column's elements to begin with.
        # The tuple will contain (value, row_index, col_index)
        minHeap = []

        for r in range(min(n, k)):
            heapq.heappush(minHeap, (matrix[r][0], r, 0))
        
        # Ensure the list maintains heap properties (though it's redundant since we're using heappush)
        heapq.heapify(minHeap)

        # Loop k times or until the heap is empty
        while k:

            # Pop the smallest element from the heap
            element, r, c = heapq.heappop(minHeap)

            # If there's another element in the same row as the just-popped element,
            # push it into the heap. This ensures we are considering the next smallest
            # element in that row for future iterations
            if c < n - 1:
                heapq.heappush(minHeap, (matrix[r][c+1], r, c+1))
            
            # Decrement k for each iteration
            k -= 1

        # The loop ends after k iterations, so the last popped element is the kth smallest element
        return element 
            

# Approach 2: Binary Search
# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
# @lc code=end

