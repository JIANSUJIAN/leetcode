#
# @lc app=leetcode id=953 lang=python3
#
# [953] Verifying an Alien Dictionary
#

# @lc code=start
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        for index, val in enumerate(order):
            order_map[val] = index

        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                # If the current index j exceeds the length of the next word,
                # it means the current word is a prefix of the next word (and is longer).
                # For example: comparing "apple" and "app". Here, the list is not sorted.
                if j >= len(words[i + 1]):
                    return False
                
                if words[i][j] != words[i + 1][j]:
                    if order_map[words[i][j]] > order_map[words[i + 1][j]]:
                        return False 
                    # Once we've found a differing character that determines the order of the two words,
                    # there's no need to check subsequent characters of these words. We break out of the 
                    # inner loop to move on to the next pair of consecutive words.
                    break
        
        return True

        
# @lc code=end

