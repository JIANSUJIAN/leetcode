#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Determine the total number of gas stations.
        n = len(gas)
        
        # This variable will keep track of the net gas after each stop.
        total = 0
        
        # Calculate the total gas remaining after each stop.
        for i in range(n):
            total += gas[i] - cost[i]
        
        # If the total remaining gas is negative, it's impossible to make a complete circuit.
        if total < 0:
            return -1
        
        # 'tank' keeps track of the gas remaining as we move from one station to the next.
        tank = 0
        # 'start' holds the index of the potential starting station.
        start = 0

        # Iterate through the gas stations.
        for i in range(n):
            tank += gas[i] - cost[i]
            
            # If the tank becomes negative, the current starting station is not valid,
            # and we need to look for a new starting station.
            if tank < 0:
                tank = 0
                start = i + 1
        
        # If 'start' equals the number of gas stations, it means we've come full circle,
        # and the start should actually be 0. Otherwise, return the value of 'start'.
        return 0 if start == n else start




        
# @lc code=end

