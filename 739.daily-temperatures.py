#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Given a list of daily temperatures, returns a list such that, 
        for each day in the input, tells you how many days you would have to wait 
        until a warmer temperature. If there is no future day for which this is possible, 
        the answer is 0.
        
        Args:
        - temperatures: List of integers representing daily temperatures.
        
        Returns:
        List of integers representing the number of days to wait for a warmer temperature.
        """
        
        # Length of the temperatures list.
        n = len(temperatures)
        
        # Initialize the result list with zeros. This will be updated with the number of days to wait.
        res = [0] * n
        
        # Use a stack to keep track of indices of temperatures for which we haven't found a warmer day yet.
        s = []
        
        # Iterate over the temperatures list in reverse to efficiently find the next warmer day using the stack.
        for i in range(n-1, -1, -1):
            
            # While there are indices in the stack and the temperature at the top of the stack 
            # is less than or equal to the current temperature, they can't be the warmer day. So, pop them off.
            while s and temperatures[s[-1]] <= temperatures[i]:
                s.pop()
            
            # If the stack isn't empty after the above operation, the index at the top of the stack 
            # represents the next warmer day. Calculate the difference in days.
            # Otherwise, there is no warmer day, so the answer remains 0.
            res[i] = s[-1] - i if s else 0
            
            # Push the current index to the stack as we move to the next iteration.
            s.append(i)
        
        return res
        
# @lc code=end

