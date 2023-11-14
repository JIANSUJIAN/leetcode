#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#

# @lc code=start
class Solution:
    def reverse(self, l: list, left: int, right: int) -> None:

        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = end = 0

        while start < n:
            while end < n and l[end] != ' ':
                end += 1
            
            self.reverse(l, start, end - 1)
            start = end + 1
            end += 1

    def reverseWords(self, s: str) -> str:

        l = list(s)
        self.reverse_each_word(l)
        return ''.join(l)

        
# @lc code=end

