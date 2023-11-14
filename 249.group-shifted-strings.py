#
# @lc app=leetcode id=249 lang=python3
#
# [249] Group Shifted Strings
#

# @lc code=start
from typing import List
import collections

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        def shift_letter(letter: str, shift: int) -> str:
            """
            Shift the given letter by the specified shift amount, considering
            circular shifts from 'z' to 'a'.
            
            Parameters:
            - letter (str): The letter to be shifted.
            - shift (int): The amount to shift the letter by.
            
            Returns:
            str: The shifted letter.
            """
            return chr((ord(letter) - shift) % 26 + ord('a'))
        
        def get_hash(string: str) -> str:
            """
            Generate a unique hash for a string, which is formed by shifting
            its letters so that the first letter becomes 'a'. All strings that
            belong to the same shifting sequence will generate the same hash.
            
            Parameter:
            - string (str): The input string.
            
            Returns:
            str: The generated hash for the string.
            """
            # Calculate the number of shifts to make the first character to be 'a'
            shift = ord(string[0])
            # Construct the hash by shifting each letter in the string
            return ''.join(shift_letter(letter, shift) for letter in string)
        
        # A defaultdict for grouping strings. Each key is a hash representing a 
        # shifting sequence, and the corresponding value is a list of strings
        # that belong to that shifting sequence.
        groups = collections.defaultdict(list)
        
        # Iterate through all the strings, and group them based on their hash
        for string in strings:
            hash_key = get_hash(string)
            # Append the string to the appropriate group
            groups[hash_key].append(string)
        
        # Return the grouped strings as a list of lists
        return list(groups.values())

        
# @lc code=end

