class Solution(object):
    def majorityElement(self, nums):
        dict={}
        b=int((len(nums)+1)/2)
        for i in nums:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
        for j in dict.values():
            if j>=b:
                for k,v in dict.items() :
                    if v==j:
                        return k
