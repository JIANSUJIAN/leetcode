#
# @lc app=leetcode id=1868 lang=python3
#
# [1868] Product of Two Run-Length Encoded Arrays
#

# @lc code=start
class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:

        i = j = 0
        product = []

        while i < len(encoded1) and j < len(encoded2):

            val1, freq1 = encoded1[i]
            val2, freq2 = encoded2[j]

            product.append([val1 * val2, min(freq1, freq2)])

            encoded1[i][1] -= min(freq1, freq2)
            encoded2[j][1] -= min(freq1, freq2)

            if encoded1[i][1] == 0: i += 1
            if encoded2[j][1] == 0: j += 1

        
        compressed_product = []
        for val, freq in product:
            if compressed_product and  compressed_product[-1][0]  == val:
                compressed_product[-1][1] += freq
            else:
                compressed_product.append([val, freq])
            
        return compressed_product

        
# @lc code=end

