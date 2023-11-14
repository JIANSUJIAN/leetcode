#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """
        Given a circular array, finds the next greater element for every element in the array.
        
        A circular array means the end of the array connects to the beginning.
        
        Args:
        - nums: List of integers.
        
        Returns:
        List of integers where each element is the next greater element in the circular array for the corresponding element in `nums`. 
        If no such element exists, the value is -1.
        """
        
        # Determine the length of the nums list.
        n = len(nums)
        
        # Initialize the result list with -1, assuming there's no next greater element for each number.
        res = [-1]*n
        
        # Use a stack to keep track of indices of numbers for which we haven't found a next greater element yet.
        s = []
        
        # Iterate over the list twice (because it's circular) in reverse order. 
        # The modulo operation helps us loop back to the beginning of the array.
        for i in range(2*n-1, -1 , -1):
            
            # While there are indices in the stack and the number at the top of the stack 
            # is less than or equal to the current number, they can't be the next greater element. So, pop them off.
            while s and s[-1] <= nums[i % n]:
                s.pop()
            
            # If the stack isn't empty after the above operation, the number at the top of the stack 
            # is the next greater element for the current number.
            # Otherwise, the result remains -1 for that position.
            res[i % n] = s[-1] if s else -1
            
            # Push the current number to the stack as we move to the next iteration.
            s.append(nums[i % n])
        
        return res
# @lc code=end

