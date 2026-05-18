# Problem: Product of Array Except Self
# Platform: LeetCode
# Difficulty: Medium
# Concepts: Hash Map

class Solution(object):
    def productExceptSelf(self, nums):
        product=1
        count=0
        flag=0
        for i in range(len(nums)):
            product*=nums[i]
            if nums[i]==0:
                count+=1
                flag=i
        if product!=0:
            arr=[]
            for i in range(len(nums)):
                arr.insert(len(arr),product/nums[i])
            return arr
        else:
            if count==1:
                arr=[0]*len(nums)
                f=1
                for i in nums:
                    if i==0:
                        continue
                    f*=i
                arr[flag]=f
                return arr
            else:
                arr=[0]*len(nums)
                return arr

"""
Time Complexity: O(n)
Space Complexity: O(n)
""""
