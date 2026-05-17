# Problem: Top K Frequent Elements
# Platform: LeetCode
# Difficulty: Medium
# Concepts: Hash Map
#NEED ALOT IMPROVEMENT IN CODE
class Solution(object):
    def topKFrequent(self, nums, k):
        dict={}
        for j in nums:
            if j in dict:
                dict[j]+=1
            else:
                dict[j]=1
        list=[]
        list2=[]
        for i in dict.values():
            list2.insert(len(list2),i)
        for i in range(0,k):
            maxt= max(list2)
            list2.remove(maxt)
            for y,z in dict.items():
                if z==maxt:
                    maxj=y
                    break
            del dict[maxj]
            list.insert(len(list),maxj)
        return list

"""
Time Complexity: 
Space Complexity: 
""""
