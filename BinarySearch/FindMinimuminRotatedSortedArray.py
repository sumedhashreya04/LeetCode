#Find Minimum in Rotated Sorted Array
class Solution(object):
    def findMin(self, nums):
        i=0 
        while (i+1<len(nums) and nums[i]<nums[i+1]):
            i+=1
        if i==len(nums)-1:
            return nums[0]
        else:
            return nums[i+1]
