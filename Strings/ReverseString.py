# Problem: Reverse String
# Platform: LeetCode
# Difficulty: Easy
# Concepts: Swapping
#Can Improve Complexity
class Solution(object):
    def reverseString(self, s):
        for i in range(int(len(s)/2)):
            a=s[i]
            s[i]=s[len(s)-1-i]
            s[len(s)-1-i]=a
