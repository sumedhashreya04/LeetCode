# Problem: Two Sum
# Platform: LeetCode
# Concepts: Hash Map

class Solution(object):
    def containsDuplicate(self, nums):
        d={}
        for i in nums:
            if i in d:
                return True
            else:
                d[i]=1
        return False

"""
Time Complexity: O(n)
Space Complexity: O(n)

Learned:
-Brute force logic implementation
- How hashmap helps reduce nested loops
"""
