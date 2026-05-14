# Problem: Two Sum
# Platform: LeetCode
# Difficulty: Easy
# Concepts: Hash Map
##BRUTE FORCE
class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0,len(nums),1):
            first=nums[i]
            second=target-first
            for j in range(i+1,len(nums)):
                if(nums[j]==second):
                    Lists=[j,i]
                    return Lists

"""
Time Complexity: O(n2)
Space Complexity: O(1)
""""
#Using Hash maps
class Solution(object):
    def twoSum(self, nums, target):
        dic={}
        for j in range(len(nums)):
            second=target-nums[j]
            if second in dic:
                return [j,dic[second]]
            else:
                dic[nums[j]]=j
"""
Time Complexity: O(n)
Space Complexity: O(n)
""""
""""
Learned:
-Brute force logic implementation
- How hashmap helps reduce nested loops
- How to think in complements
"""
