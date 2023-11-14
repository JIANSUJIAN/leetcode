#
# @lc app=leetcode id=408 lang=python3
#
# [408] Valid Word Abbreviation
#

# @lc code=start
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = len(word), len(abbr)
        multiplier, prev_digit = 1, None

        while i > 0 and j > 0:
            c1 = word[i-1]
            c2 = abbr[j-1]

            if c1 == c2:
                i -= 1
                j -= 1
                multiplier = 1
                if prev_digit == 0:
                    return False
            elif c2.isdigit():
                i -= int(c2)*multiplier
                j -= 1
                multiplier *= 10
                prev_digit = int(c2)
            else:
                return False
        
        return i == j == 0


        
# @lc code=end

