#BRUTE Force approach
class Solution(object):
    def maxSubArray(self, nums):
        max=float('-inf')
        for j in range(1,len(nums)+1):
          for k in range(0,len(nums)-(j-1)):
            sum=0
            for l in range(k,k+j):
               sum+=nums[l]
            if sum>max:
                max=sum
        return max
#Time complexity O(n3)
#Need to find optimised solution not studied dsa implementation working on it
