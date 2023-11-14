#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#

# @lc code=start

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:

        # char_freq = {}
        # for char in s:
        #     char_freq[char] = char_freq.get(char, 0) + 1

        char_freq = Counter(s)
        
        
        for idx, char in enumerate(s):
            if char_freq[char] == 1:
                return idx
        return -1
        
# @lc code=end

