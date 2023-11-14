#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # Convert the string into an array of integers for easier hashing.
        # 'A' -> 0, 'G' -> 1, 'C' -> 2, 'T' -> 3
        nums = [0] * len(s)
        for i in range(len(nums)):
            if s[i] == 'A':
                nums[i] = 0
            elif s[i] == 'G':
                nums[i] = 1
            elif s[i] == 'C':
                nums[i] = 2
            elif s[i] == 'T':
                nums[i] = 3
        
        # Set to store sequences (in hash form) that we've seen so far.
        seen = set()
        
        # Set to store sequences that are repeated.
        res = set()

        # Constants for the rolling hash algorithm.
        L = 10  # length of the DNA sequence
        R = 4   # radix/base value (since there are 4 possible characters in the DNA sequence)
        RL = R ** (L - 1)  # maximum power for the radix/base value
        
        # Initialize the rolling hash value.
        windowHash = 0 

        # Pointers to mark the start and end of the current 10-letter sequence.
        left, right = 0, 0

        # Slide the window through the entire DNA sequence.
        while right < len(nums):
            # Update the hash by removing the leftmost digit and adding the rightmost digit.
            windowHash = windowHash * R + nums[right]
            right += 1

            # When the window size is L (10 in this case), check if it's a repeated sequence.
            if right - left == L:
                # If this hash was seen before, it's a repeated sequence.
                if windowHash in seen:
                    res.add(s[left:right])
                else:
                    # Otherwise, mark this sequence as seen.
                    seen.add(windowHash)
                
                # Remove the leftmost value from the hash and move the left pointer one step.
                windowHash -= nums[left] * RL
                left += 1
        
        # Convert the set of repeated sequences to a list before returning.
        return list(res)


        
# @lc code=end

