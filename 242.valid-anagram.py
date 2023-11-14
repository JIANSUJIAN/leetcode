#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)

        for x in s:
            count[x] += 1
        for x in t:
            count[x] -= 1
        for val in count.values():
            if val != 0:
                return False
        
        return True

        
# @lc code=end

