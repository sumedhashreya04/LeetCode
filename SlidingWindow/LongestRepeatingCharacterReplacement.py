##Time Limit Exceeded \\O(n)=O(50n):Hint
#Need improvement \\
#Redo-LongestRepeatingCharacterReplacement
class Solution(object):
    def characterReplacement(self, s, k):
        if k+1>=len(s):
            return len(s)
        for i in range(k+2,len(s)+1):
            llcase=0
            if i==len(s):
                llcase=1
            for j in range(len(s)-i+1):
                dicti={}
                lcase=0
                if j==len(s)-i:
                    lcase=1
                for l in range(j,j+i):
                    if s[l] in dicti:
                        dicti[s[l]]+=1
                    else:
                        dicti[s[l]]=1
                maxkey=max(dicti,key=dicti.get)
                del dicti[maxkey]
                sum=0
                for l in dicti.values():
                    sum+=l
                if sum<=k:
                    if llcase==1:
                        return i
                    break
                if lcase==1:
                    return i-1
