#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()

        # Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)
        
        # create a seperate set for nagatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        # If there is at least 1 zero in the list, add  combinations where
        # the negative counterpart of a positive number exisits.
        if z:
            for num in P:
                if -num in N:
                    res.add((-num, 0, num))
        
        # If there are at least three zeroes in the list, include the triplet (0, 0, 0)
        if len(z) >= 3:
            res.add((0, 0, 0))

        # For each combination of two negative numbers, check if
        # there exisits a postive number which makes the sum zero.
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                complement = -1 * (n[i] + n[j])
                if complement in P:
                    res.add(tuple(sorted([n[i], n[j], complement])))
        
        # For each combination of two positive numbers, check if 
        # there exists a nagative number which makes the sume zero.
        for i in range(len(p)):
            for j in range(i+1, len(p)):
                complement = -1 * (p[i] + p[j])
                if complement in N:
                    res.add(tuple(sorted([p[i], p[j], complement])))
                            
        return res


        
# @lc code=end

