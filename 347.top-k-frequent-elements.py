#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Create a dictionary to store the frequency of each number in the nums list.
        valToFreq = {}
        for num in nums:
            valToFreq[num] = valToFreq.get(num, 0) + 1

        # Initialize an empty priority queue (min-heap) to store the numbers based on their frequencies.
        pq = []
        
        # Iterate over each unique number and its frequency.
        for num, freq in valToFreq.items():
            # Push the (frequency, number) tuple into the heap. 
            # This ensures that the heap is primarily sorted by frequency.
            heapq.heappush(pq, (freq, num))
            
            # If the heap size exceeds k, pop the least frequent number.
            # This step ensures that our heap only contains the k most frequent numbers.
            if len(pq) > k:
                heapq.heappop(pq)
        
        # Construct the result list by extracting numbers from the heap.
        # Since the heap contains the k most frequent numbers, we extract the second element (i.e., the number) from each tuple.
        return [item[1] for item in pq]
        
        

        
# @lc code=end

