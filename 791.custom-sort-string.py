#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#

# @lc code=start
import collections


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Step 1: Use collections.Counter to get the occurrence count of each character in s.
        count = collections.Counter(s)
        ans = []

        # Step 2: For each character in 'order', append it to the ans list in the order they appear.
        for char in order:
            # Append character char to the ans list as many times as it appears in s.
            ans.append(char * count[char])
            # After processing character char, set its count to 0.
            count[char] = 0

        # Step 3: Append characters that are in s but not in order to the ans list.
        for char in count:
            ans.append(char * count[char])

        # Step 4: Convert the ans list back to a string and return.
        return "".join(ans)


# @lc code=end
