#
# @lc app=leetcode id=252 lang=python3
#
# [252] Meeting Rooms
#

# @lc code=start

# Approach 1: Brute Force
# class Solution:
#     def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

#         def overlap(interval1: List[int], interval2: List[int]) -> bool:
#             return (min(interval1[1], interval2[1]) >
#                     max(interval1[0], interval2[0]))
        
#         for i in range(len(intervals)):
#             for j in range(i + 1, len(intervals)):
#                 if overlap(intervals[i], intervals[j]):
#                     return False
#         return True
        
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()

        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        
        return True
# @lc code=end

