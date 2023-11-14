#
# @lc app=leetcode id=346 lang=python3
#
# [346] Moving Average from Data Stream
#

# @lc code=start
## 1. Array or List
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        size, queue = self.size, self.queue
        queue.append(val)

        window_sum = sum(queue[-size:])

        return window_sum/ min(len(queue), size)

## 2. Double-ended Queue

from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize the MovingAverage class.
        
        :param size: The window size for calculating the moving average.
        """
        self.size = size
        self.queue = deque()
        self.window_sum = 0
        self.count = 0

    def next(self, val: int) -> float:
        """
        Add a new integer value to the stream and return the moving average 
        of the last 'size' integer values.
        
        :param val: The new integer value to add.
        :return: The moving average of the last 'size' integer values.
        """
        # Increment the count of elements seen
        self.count += 1
        
        self.queue.append(val)

        # If the queue has more than 'size' elements, remove the oldest element
        # Otherwise, consider the oldest element (tail) as 0
        tail = self.queue.popleft() if self.count > self.size else 0
        
        # Update the sum of the window by adding the new value and subtracting the tail
        self.window_sum = self.window_sum + val - tail
        
        # Return the average of the elements in the current window
        # If the count is less than the window size, divide by count, otherwise divide by window size
        return self.window_sum / min(self.size, self.count)

