#
# @lc app=leetcode id=706 lang=python3
#
# [706] Design HashMap
#

# @lc code=start
from typing import List, Tuple

# # Approach 1: Modulo + Array

# class Bucket:
#     def __init__(self) -> None:
#         """
#         Initialize an empty bucket.
        
#         The bucket is a list containing pairs (key, value) where both are integers.
#         """
#         self.bucket: List[Tuple[int, int]] = []
    
#     def get(self, key: int) -> int:
#         """_summary_

#         Args:
#             key (int): The key to search for.

#         Returns:
#             int: The value associated with the given key. Return -1 if key is not present.
#         """
#         for (k, v) in self.bucket:
#             if k == key:
#                 return v
#         return -1
    
#     def update(self, key: int, value: int) -> None:
#         """
#         Update the value for a given key. If the key does not exist, it's added to the bucket

#         Args:
#             key (int): They key to update or add.
#             value (int): The value associated with the key
#         """
#         found = False
#         for i, (k, v) in enumerate(self.bucket):
#             if key == k:
#                 # If key exisits, update its value and set found flag to True
#                 self.bucket[i] = (key, value)
#                 found = True
#                 break
        
#         # If the key doesn't exisit, append it as a new key-value pair to the bucket
#         if not found:
#             self.bucket.append((key, value))

#     def remove(self, key):
#         """
#         Remove the pair (key, value) from the bucket.

#         Args:
#             key (int): The key to remove.
#         """
#         for i, (k, v) in enumerate(self.bucket):
#             if key == k:
#                 del self.bucket[i]
#                 return 


# class MyHashMap:

#     def __init__(self) -> None:
#         """
#         Initialzie the hash map with a fixed size of key space.

#         A prime number is used for the key space to reduce the possibility of collisons.
#         Each slot in the hash table contains a bucket.
#         """
#         self._key_space: int = 2069
#         self._hash_table: List[Bucket] = [Bucket() for _ in range(self._key_space)]

#     def put(self, key: int, value: int) -> None:
#         """
#         Inset or update a key-value pair in the hash map.

#         Args:
#             key (int): The key to insert or update
#             value (int): The value to associate with the key
#         """
#         hash_key = key % self._key_space
#         self._hash_table[hash_key].update(key, value)
        

#     def get(self, key: int) -> int:
#         """
#         Retrieve the value associated with a key from the hash map. 

#         Args:
#             key (int): The key to search for.

#         Returns:
#             int: The value associated with the key, Return -1 if the key is not found
#         """
#         hash_key = key % self._key_space
#         return self._hash_table[hash_key].get(key) 
        

#     def remove(self, key: int) -> None:
#         """
#         Remove a key-value pair from the hash map based on the provided key.

#         Args:
#             key (int): The key of the pair to remove.
#         """
#         hash_key = key % self._key_space
#         self._hash_table[hash_key].remove(key)
        

# Approach 2:  Linked List

class ListNode:
    def __init__(self, key: int, val: int):
        """
        Initialize a node in the linked list.

        Args:
            key (int): The key for the current node.
            val (int): The value associated with the key.
        """
        self.key = key
        self.value = val
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize an empty hash map with default size.
        """
        self.size = 2069
        self.buckets = [None] * self.size
    
    def _hash(self, key: int) -> int:
        """
        Compute the hash of the key to determine its index in the bucket.

        Args:
            key (int): The key to be hashed.

        Returns:
            int: The hashed index.
        """
        return key % self.size

    def put(self, key: int, value: int) -> None:
        """
        Inserts or updates a key-value pair in the hash map.

        Args:
            key (int): The key to be added or updated.
            value (int): The value to be associated with the key.
        """
        index = self._hash(key)
        if not self.buckets[index]:
            self.buckets[index] = ListNode(key, value)
        else:
            current = self.buckets[index]
            while current:
                # If the key already exists, update its value
                if current.key == key:
                    current.value = value
                    return 
                # Move to the next node if available.
                if not current.next: break
                current = current.next
            current.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Fetch the value associated with key.

        Args:
            key (int): The key to be fetched.

        Returns:
            int:  The value associated with the key. or -1 if key doesn't exist.
        """
        index = self._hash(key)
        current = self.buckets[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return -1
        

    def remove(self, key: int) -> None:
        """
        Remove a key and its associated value from the hash map.

        Args:
            key (int): The key to be removed.
        """
        index = self._hash(key)
        current = self.buckets[index]

        if not current:
            return 

        # If the key of the first node matches the target key,
        # bypass this node to remove it.
        if current.key == key:
            self.buckets[index] = current.next
            return
        
        # Ohterwise, traverse the linked list to locate the node with the target key.
        while current.next:
            # If the key of the next node matches the target key,
            # bypass the next node to remove it.
            if current.next.key == key:
                current.next = current.next.next
                return
            current = current.next

        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

