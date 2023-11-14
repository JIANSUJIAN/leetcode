#
# @lc app=leetcode id=1328 lang=python3
#
# [1328] Break a Palindrome
#

# @lc code=start
class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        length = len(palindrome)
        if length == 1:
            return ""
        
        palindromeList = list(palindrome)

        for i in range(length // 2):
            if palindromeList[i] != "a":
                palindromeList[i] = "a"
                return "".join(palindromeList)
        
        palindromeList[length - 1] = "b"
        return "".join(palindromeList)

        
# @lc code=end

