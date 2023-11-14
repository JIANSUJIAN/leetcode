#
# @lc app=leetcode id=1002 lang=python3
#
# [1002] Find Common Characters
#

# @lc code=start

from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        
        # Counter creates a dictionary-like object where each key is a unique character
        # in the given word, and its corresponding value is the count of that character.
        common = Counter(words[0])

        # Iterate over the remaining words in the list (skipping the first word).
        for word in words[1:]:
            
            # Convert the current word to a Counter.
            wordCounter = Counter(word)

            # Iterate over the keys (unique characters) in the 'common' Counter.
            # We convert the keys view to a list to avoid "dictionary size changed during iteration" error.
            for key in list(common.keys()):
                # If the character (key) exists in the current word's Counter:
                if key in wordCounter:
                    # Update the count in 'common' to be the minimum of the counts in 
                    # both 'common' and the current word's Counter. This ensures that 
                    # the 'common' Counter only keeps characters that are present in all words so far.
                    common[key] = min(common[key], wordCounter[key])
                else:
                    # If the character doesn't exist in the current word's Counter,
                    # remove it from 'common' as it's not common to all words.
                    del common[key]

        # The elements() method of Counter returns an iterator over elements repeating 
        # as many times as their count. Convert this iterator to a list to get the final result.
        return list(common.elements())


        
# @lc code=end

