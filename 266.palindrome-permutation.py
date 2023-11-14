#
# @lc app=leetcode id=266 lang=python3
#
# [266] Palindrome Permutation
#

# @lc code=start
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        charMap = {}

        for ch in s:
            charMap[ch] = charMap.get(ch, 0) + 1

        odd_count = sum(freq % 2 for freq in charMap.values())

        return odd_count <= 1
        
# @lc code=end

