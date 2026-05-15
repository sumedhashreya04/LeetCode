# Problem: Longest Common Prefix
# Platform: LeetCode
# Difficulty: Easy
# Concepts: Slicing
class Solution(object):
    def longestCommonPrefix(self, strs):
        order=min(strs,key=len)
        for i in range(len(strs)):
            for j in range(len(order)):
                if strs[i][j]!=order[j]:
                    order=order[:j]
                    break
        return order

"""
Space Complexity: O(1)
""""
