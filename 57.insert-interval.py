#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#

# @lc code=start

# Approach 1: Linear Search
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:
            return [newInterval]

        res = []
        inserted = False

        for interval in intervals:

            if interval[0] > newInterval[1] and not inserted:
                res.append(newInterval)
                inserted = True
            if newInterval[1] < interval[0] or interval[1] < newInterval[0]:
                res.append(interval) 
            else:
                newInterval[0] = min(newInterval[0], interval[0])
                newInterval[1] = max(newInterval[1], interval[1])
            
        if not inserted:
            res.append(newInterval)
    
        return res
    
# Approach 2: Binary Search
# @lc code=end

