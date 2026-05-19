# Problem: 3Sum
# Platform: LeetCode
# Difficulty: Medium
# Concepts: Two Pointer
#EXCEEDING TIME LIMIT 
#NEED TO THINK ANOTHER APPROACH
#100 CASES FAILED
from collections import Counter

class Solution(object):
    def threeSum(self, nums):
        mlist=[]
        for k in range(len(nums)-2):
            for j in range(k+1,len(nums)-1):               
                for i in range(j+1,len(nums)):
                    if nums[i]+nums[k]+nums[j]==0:
                        list=[nums[i],nums[j],nums[k]]
                        flag=0
                        for l in range(len(mlist)):
                            if Counter(mlist[l])==Counter(list):
                                flag+=1
                        if flag==0 or len(mlist)==0:
                            mlist.insert(len(mlist),list)
        return mlist

"""
Time Complexity: O(m3)
Space Complexity: O(1)
