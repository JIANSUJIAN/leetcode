#
# @lc app=leetcode id=1570 lang=python3
#
# [1570] Dot Product of Two Sparse Vectors
#

# @lc code=start

# Approach 2: Hash Set
# class SparseVector:
#     def __init__(self, nums: List[int]):
#         self.nonzeros = {}
#         for i, n in enumerate(nums):
#             if n != 0:
#                 self.nonzeros[i] = n

#     # Return the dotProduct of two sparse vectors
#     def dotProduct(self, vec: 'SparseVector') -> int:
#         res = 0 
#         for i, n in self.nonzeros.items():
#             if i in vec.nonzeros:
#                 res += n * vec.nonzeros[i]
        
#         return res

# Approach 3: Index-Value pairs (two pointers)
class SparseVector:
    def __init__(self, nums: List[int]):
        self.pairs = []
        for i, n in enumerate(nums):
            if n != 0:
                self.pairs.append([i, n])
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        p, q = 0, 0

        while p < len(self.pairs) and q < len(vec.pairs):
            if self.pairs[p][0] == vec.pairs[q][0]:
                res += self.pairs[p][1] * vec.pairs[q][1]
                p += 1
                q += 1
            elif self.pairs[p][0] < vec.pairs[q][0]:
                p += 1
            else:
                q += 1
        return res
        


        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
# @lc code=end

