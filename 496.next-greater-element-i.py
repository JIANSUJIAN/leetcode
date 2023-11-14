#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:

    def nextGreater(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Initialize result list with zeros. This will be updated to store the next greater element for each position.
        res = [0 for _ in range(n)]

        # Use a stack to keep track of elements whose next greater element hasn't been found yet.
        s = []

        # Iterate over the list in reverse to efficiently find the next greater element using the stack.
        for i in range(n - 1, -1 , -1): 

            # While there are elements in the stack and the top element is less than or equal to the current element,
            # they can't be the next greater element. So, pop them off.
            while s and s[-1] <= nums[i]:
                s.pop()

            # If the stack isn't empty after the above operation, its top element is the next greater element for nums[i].
            # Otherwise, there is no next greater element, so assign -1.
            res[i] = s[-1] if s else -1

            # Push the current element to the stack as we move to the next iteration.
            s.append(nums[i])

        return res  # This should return 'res' instead of 's' to get the desired output.

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        # Find the next greater element for each element in nums2.
        greater = self.nextGreater(nums2)
        
        # Create a mapping from each element in nums2 to its next greater element.
        greaterMap = {}
        for i in range(len(nums2)):
            greaterMap[nums2[i]] = greater[i]
        
        # Initialize the result list.
        res = [0] * len(nums1)
        
        # For each element in nums1, fetch its next greater element from the mapping.
        for i in range(len(nums1)):
            res[i] = greaterMap[nums1[i]]
        
        return res


        
# @lc code=end

