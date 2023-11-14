#
# @lc app=leetcode id=1019 lang=python3
#
# [1019] Next Greater Node In Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # Extract the values from the linked list into a list called 'values'.
        values = []
        while head:
            values.append(head.val)
            head = head.next
        
        # Initialize the answer list with zeros. This will store the next larger values for each node.
        answer = [0] * len(values)
        
        # Use a stack to keep track of indices of values for which we haven't found a larger value yet.
        stack = []

        # Traverse through the 'values' list.
        for i, value in enumerate(values):
            # Check if the current value is greater than the value at the index stored at the top of the stack.
            # If yes, we've found the next larger value for that index.
            while stack and values[stack[-1]] < value:
                smaller = stack.pop()  # Pop the index for which we've found a larger value.
                answer[smaller] = value  # Update the answer list with the larger value.
            
            # Push the current index onto the stack to look for its next larger value in subsequent iterations.
            stack.append(i)

        # Return the final answer list with next larger values.
        return answer

        
# @lc code=end

