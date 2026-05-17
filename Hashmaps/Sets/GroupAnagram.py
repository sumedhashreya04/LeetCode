# Problem: Group Anagram
# Platform: LeetCode
# Difficulty: Medium
# Concepts: Hash Map
#*Need to improve later*
#*Very high running Time 
class Solution(object):
    def groupAnagrams(self, strs):
        dict2={}
        dict1={}
        for i in strs:
            d={}
            for j in i:
                if j in d:
                    d[j]+=1
                else:
                    d[j]=1
            if dict2=={}:
                dict2[i]=d
                dict1[i]=[i]
            else:
                bool=False
                for k,v in dict2.items():
                    if v==d :
                        dict1[k].append(i)
                        bool=True
                else:
                    if bool==False:
                        dict2[i]=d
                        dict1[i]=[i]
        mlist=[]
        for i in dict1.values():
            mlist.append(i)
        return mlist

"""
Time Complexity: High
Space Complexity: O(1)
""""
