#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.stk = []
        self.minstk = []
        
    def push(self, val: int) -> None:
        self.stk.append(val)
        if not self.minstk or val <= self.minstk[-1]:
            self.minstk.append(val)

    def pop(self) -> None:
        if self.stk[-1] == self.minstk[-1]:
            self.minstk.pop()
        self.stk.pop()
        
    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minstk[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

