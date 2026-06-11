class Solution(object):
    def search(self, nums, target):
        st=0
        end=len(nums)-1
        while st<=end:
            mid=(st+end)/2
            if nums[mid]<target:
                st=mid+1
            elif nums[mid]>target:
                end=mid-1
            else:
                return mid
        return -1
