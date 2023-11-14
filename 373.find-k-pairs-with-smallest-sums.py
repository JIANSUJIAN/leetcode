#
# @lc app=leetcode id=373 lang=python3
#
# [373] Find K Pairs with Smallest Sums
#

# @lc code=start
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Edge case: If either nums1 or nums2 is empty, we can't form any pairs.
        if not nums1 or not nums2:
            return []

        # Initialize a priority queue (min heap).
        # Each element in the heap is a tuple of (sum of pair, index in nums1, index in nums2).
        # At the start, we pair the first element of nums1 with each element of nums2.
        min_heap = [(nums1[0] + n, 0, idx) for idx, n in enumerate(nums2)]
        heapq.heapify(min_heap)

        res = []

        # We loop until we've found k pairs or the heap is exhausted.
        while min_heap and k > 0:
            # Extract the pair with the smallest sum.
            val, i, j = heapq.heappop(min_heap)

            # Append the corresponding values from nums1 and nums2 to the result.
            res.append([nums1[i], nums2[j]])

            # If there exists another number in nums1 to pair with the current number from nums2, 
            # add that new pair to the heap.
            if i + 1 < len(nums1):
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))

            # Decrement k since we've added one more pair to the result.
            k -= 1

        return res



            


# @lc code=end

