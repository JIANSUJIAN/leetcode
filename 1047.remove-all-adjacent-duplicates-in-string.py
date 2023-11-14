#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#

# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        output = []

        for ch in s:
            if output and ch == output[-1]:
                output.pop()
            else:
                output.append(ch)
        return ''.join(output)


        
# @lc code=end

