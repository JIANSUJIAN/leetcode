#
# @lc app=leetcode id=824 lang=python3
#
# [824] Goat Latin
#

# @lc code=start
class Solution:
    def toGoatLatin(self, sentence: str) -> str:

        def is_vowel(ch: str) -> bool:
            return ch.lower() in ('a', 'e', 'i', 'o', 'u')
        
        words = sentence.split()

        for i, word in enumerate(words):
            if is_vowel(word[0]):
                words[i] = word + "ma" 
            else:
                words[i] = word[1:] + word[0] + "ma" 
            
            words[i] += 'a' * (i + 1)

        return ' '.join(words)
        
# @lc code=end

