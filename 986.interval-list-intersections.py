#
# @lc app=leetcode id=986 lang=python3
#
# [986] Interval List Intersections
#

# @lc code=start

from typing import List

from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        Return the intersection of two lists of intervals.
        
        Args:
        - firstList: List of intervals from the first set.
        - secondList: List of intervals from the second set.
        
        Returns:
        - List of intervals that represent the intersection of the two input lists.
        """

        # Two pointers to iterate through the two lists
        i, j = 0, 0
        # To store the resultant intersected intervals
        res = []

        # Continue until one of the lists runs out of intervals
        while i < len(firstList) and j < len(secondList):
            # Unpack intervals from the two lists for easy comparison
            a1, a2 = firstList[i]
            b1, b2 = secondList[j]

            # If the end of the current interval in secondList is greater than 
            # or equal to the start of the current interval in firstList, and 
            # the end of the current interval in firstList is greater than 
            # or equal to the start of the current interval in secondList, 
            # then the two intervals intersect.
            if b2 >= a1 and a2 >= b1:
                # Add the intersected part to the result.
                res.append([max(a1, b1), min(a2, b2)])

            # Move the pointer that points to the smaller end value
            # as we are done considering all intersections for that particular interval.
            if b2 < a2:
                j += 1
            else:
                i += 1

        # Return the list of intersections
        return res

        
# @lc code=end

