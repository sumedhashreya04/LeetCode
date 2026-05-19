# Problem: Two Sum II
# Platform: LeetCode
# Difficulty: Medium
# Concepts: Two Pointers
class Solution(object):
    def twoSum(self, numbers, target):
        start=0
        end=len(numbers)-1
        while end!=start:
            if(numbers[start]+numbers[end]>target):
                end-=1
            elif(numbers[start]+numbers[end]<target):
                start+=1
            else:
                return [start+1,end+1]

"""
Time Complexity: O(n)
Space Complexity: O(1)
