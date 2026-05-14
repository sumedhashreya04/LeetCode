# Problem: Move Zeroes
# Platform: LeetCode
# Difficulty: Easy
# Concepts: Two Pointer
class Solution(object):
    def moveZeroes(self, nums):
        ptr=0
        for i in range(0,len(nums)):
           if(nums[i]!=0):
            a=nums[i]
            nums[i]=nums[ptr]
            nums[ptr]=a
            ptr+=1

"""
Time Complexity: O(n)
Space Complexity: O(1)

Learned:
-Brute force logic implementation
- How two pointer helps reduce nested loops
"""
