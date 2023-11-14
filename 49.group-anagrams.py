#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to map the unique encoding of anagrams to the groups of words that match the encoding.
        encoding_to_group = {}

        for word in strs:
            # Generate a unique encoding for each word based on character counts.
            word_encoding = self.generateEncoding(word)

            # Check if the unique encoding of the word (word_encoding) already exists as a key in the dictionary.
            if word_encoding not in encoding_to_group:
                # If not, initialize the key with an empty list. 
                # This list will store all words that have the same encoding (i.e., are anagrams).
                encoding_to_group[word_encoding] = []

            # Add the current word to the list corresponding to its encoding.
            # This groups the word with its potential anagrams in the dictionary.
            encoding_to_group[word_encoding].append(word)       

        # Convert the grouped words from dictionary values to a list of lists.
        return list(encoding_to_group.values())

    def generateEncoding(self, word: str) -> str:
        # Create a list `alphabet_count` to keep track of the frequency of each character in the word.
        # We use a list of 26 zeros because there are 26 letters in the alphabet.
        # Each position in the list corresponds to a letter in the alphabet, i.e., 0 -> 'a', 1 -> 'b', ..., 25 -> 'z'.
        alphabet_count = [0] * 26

        # For each character in the word:
        for char in word:
            # Compute the index in the `alphabet_count` list where this character should be counted.
            # Subtracting ord('a') normalizes our ord value, turning 'a' -> 0, 'b' -> 1, ..., 'z' -> 25.
            index = ord(char) - ord('a')

            # Increment the count for this character in the `alphabet_count` list.
            alphabet_count[index] += 1

        # Convert the list of counts to a string. This string serves as a unique encoding for anagrammatic words.
        # For instance, "aabb" and "abab" will both convert to "[2, 2, ...]", where the "2" at positions 0 and 1
        # indicates that there are two 'a's and two 'b's respectively in the word.
        return str(alphabet_count)

        
# @lc code=end

