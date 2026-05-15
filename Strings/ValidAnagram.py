# Problem: Valid Anagram
# Platform: LeetCode
# Difficulty: Easy
# Concepts: Hash Map/Dictionaries
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
          return False
        dic={}
        for l in s:
            if l in dic :
                dic[l]+=1
            else:
                dic[l]=1
        for m in t:
            if m in dic:
                dic[m]-=1
                if dic[m]==0:
                    del dic[m]           
            else:
                return False
        if not dic:
            return True

"""
Time Complexity: O(n)
Space Complexity: O(1)
""""
