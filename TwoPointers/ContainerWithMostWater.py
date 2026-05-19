# Problem: Container With Most Water
# Platform: LeetCode
# Difficulty: Medium
# Concepts: Two pointers
class Solution(object):
    def maxArea(self, height):
        start=0
        maxi=0
        end=len(height)-1
        while start!=end:
            if ((end-start)*min(height[start],height[end]))>maxi:
                maxi=((end-start)*min(height[start],height[end]))
            if height[start]>=height[end]:
                end-=1
            else:
                start+=1
        return maxi

"""
Time Complexity: O(n)
Space Complexity: O(1)
