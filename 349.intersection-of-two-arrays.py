#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1, nums2):
        """
        Find the intersection of two arrays.

        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """  
        
        # Convert 'nums1' to a set. Sets in Python are unordered collections of unique elements.
        # By converting to a set, we remove duplicates and can perform O(1) lookups.
        set1 = set(nums1)
        
        # Convert 'nums2' to a set for the same reasons.
        set2 = set(nums2)
        
        # Find the intersection of the two sets.
        # The '&' operator returns a set containing all elements that are present in both sets.
        intersection_set = set1 & set2
        
        # Convert the resulting set back to a list.
        # Lists are ordered collections and are typically easier to work with in many contexts.
        # Here, we return the intersection as a list.
        return list(intersection_set)
      
# @lc code=end

