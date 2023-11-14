#
# @lc app=leetcode id=752 lang=python3
#
# [752] Open the Lock
#

# @lc code=start

from typing import List
from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        deads = set(deadends)
        visited = set()
        q = deque()
        turns = 0

        q.append("0000")
        visited.add("0000")

        while q:
            sz = len(q)
            for _ in range(sz):
                cur = q.popleft()
                if cur in deads:
                    continue
                if cur == target:
                    return turns
                
                for j in range(4):
                    up = self.plusOne(cur, j)
                    if up not in visited:
                        q.append(up)
                        visited.add(up)
                    down = self.minusOne(cur, j)
                    if down not in visited:
                        q.append(down)
                        visited.add(down)
            turns += 1
        return -1

    def plusOne(self, s:str, j: int) -> str:
        ch = list(s)
        if ch[j] == "9":
            ch[j] = "0"
        else:
            ch[j] = str(int(ch[j]) + 1)
        return "".join(ch)
    
    def minusOne(self, s: str, j:int) -> str:
        ch = list(s)
        if ch[j] == "0":
            ch[j] = "9"
        else:
            ch[j] = str(int(ch[j]) - 1)
        return "".join(ch)
                

        
# @lc code=end

