#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#

# @lc code=start

from queue import Queue

class MyStack:
    def __init__(self):
        # Queue to simulate stack operations
        self.q = Queue()
        
        # Variable to store the top element of the stack
        self.top_elem = 0

    def push(self, x: int) -> None:
        # Add the element to the end of the queue
        # and update the top element
        self.q.put(x)
        self.top_elem = x

    def pop(self) -> int:
        # Get the current size of the queue
        size = self.q.qsize()

        # Rotate the queue until only the last two inserted elements 
        # are at the front. This is done to access the top of the stack 
        # (i.e., the last inserted element in the queue).
        while size > 2:
            # Move the front element to the back of the queue
            self.q.put(self.q.get())
            
            # Decrement the size counter
            size -= 1

        # Update the top_elem to the next top of the stack.
        # This is the second last inserted element.
        self.top_elem = self.q.queue[0]

        # Move the current top of the stack (last inserted element) 
        # to the back of the queue
        self.q.put(self.q.get())
        
        # Dequeue and return the new front element, which is the 
        # original top of the stack
        return self.q.get()

    def top(self) -> int:
        # Return the top element of the stack
        return self.top_elem

    def empty(self) -> bool:
        # Return True if the queue is empty, i.e., the stack is empty
        return self.q.empty()



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

