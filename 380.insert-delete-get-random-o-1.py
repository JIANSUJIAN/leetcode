#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
class RandomizedSet:
    import random
    def __init__(self):
        # Initialize an empty dictionary to store the values and their indices in the list.
        self.val_to_index = {}
        # Initialize an empty list to store the value.
        self.values = []
        

    def insert(self, val: int) -> bool:
        # If the value is already in the dictionary, return False
        if val in self.val_to_index:
            return False
        
        # Otherwise, add the value to the list
        self.values.append(val)
        # Store the index of the value in the dicitonary.
        self.val_to_index[val] = len(self.values) - 1

        return True
        

    def remove(self, val: int) -> bool:

        # If the value is not in the dictionary, return False
        if val not in self.val_to_index:
            return False
        
        # Get the last value in the 'values' list. This value will be used to
        # take the place of the value we want to remove, ensuring we can remove
        # the value in constant time by popping from the end of the list.
        last_val = self.values[-1]
        
        # Get the index of the value we want to remove from the 'val_to_index' dictionary.
        idx = self.val_to_index[val]
        
        # Swap the positions of 'val' and the last value in the 'values' list.
        # Simultaneously, update the index for 'last_val' in the 'val_to_index' 
        # dictionary to point to the original position of 'val'.
        self.values[idx], self.val_to_index[last_val] = last_val, idx

        # Remove the last value from the list
        self.values.pop()
        # Delete the value from the dictionary.
        del self.val_to_index[val]

        return  True

    def getRandom(self) -> int:
        return random.choice(self.values)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

