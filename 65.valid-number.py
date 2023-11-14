#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#

# @lc code=start
class Solution:
    def isNumber(self, s: str) -> bool:
        seen_dot = seen_exp = seen_digit = False

        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in ["+", "-"]:
                if i > 0 and s[i-1] != "e" and s[i-1] != "E":
                    return False
            elif c in ["e", "E"]:
                if seen_exp or not seen_digit:
                    return False
                seen_exp = True
                seen_digit = False
            elif c == ".":
                if seen_dot or seen_exp:
                    return False
                seen_dot = True
            else:
                return False
        return seen_digit
            


        
# @lc code=end

