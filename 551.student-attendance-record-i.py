#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        countA = 0
        n = len(s)
        i = 0

        while i < n and countA < 2:
            if s[i] == 'A':
                countA += 1
            if i <= n - 3 and s[i:i+3] == 'LLL':
                return False
            i += 1
        return countA < 2
        
# @lc code=end

