#
# @lc app=leetcode id=2259 lang=python3
#
# [2259] Remove Digit From Number to Maximize Result
#

# @lc code=start
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans = 0 

        for i, dig in enumerate(number):
            if dig == digit:
                ans = max(ans, int(number[:i] + number[i + 1:]))
        
        return str(ans)

        
# @lc code=end

