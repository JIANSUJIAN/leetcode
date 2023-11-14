#
# @lc app=leetcode id=2068 lang=python3
#
# [2068] Check Whether Two Strings are Almost Equivalent
#


# @lc code=start
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26

        for char in word1:
            freq1[ord(char) - ord("a")] += 1

        for char in word2:
            freq2[ord(char) - ord("a")] += 1

        for i in range(26):
            if abs(freq1[i] - freq2[i]) > 3:
                return False

        return True


# @lc code=end
