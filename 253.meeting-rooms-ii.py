#
# @lc app=leetcode id=253 lang=python3
#
# [253] Meeting Rooms II
#

# @lc code=start
import heapq
# Approach 1: Priority Queues
# class Solution:
#     def minMeetingRooms(self, intervals: List[List[int]]) -> int:

#         if not intervals:
#             return 0
        
#         intervals.sort(key= lambda x: x[0])

#         free_rooms = []

#         heapq.heappush(free_rooms, intervals[0][1])

#         for meeting in intervals[1:]:
#             if free_rooms[0] <= meeting[0]:
#                 heapq.heappop(free_rooms)
#             heapq.heappush(free_rooms, meeting[1])

#         return len(free_rooms)



# Approach 2: Chronological Ordering (two pointers)
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        if not intervals:
            return 0
        
        used_room = 0

        starting_times = sorted(i[0] for i in intervals)
        ending_times = sorted(i[1] for i in intervals)

        start_pointer = 0
        end_pointer = 0

        while start_pointer < len(intervals):
            if starting_times[start_pointer] >= ending_times[end_pointer]:
                used_room -= 1
                end_pointer += 1
            
            used_room += 1
            start_pointer += 1
        
        return used_room


        
# @lc code=end

