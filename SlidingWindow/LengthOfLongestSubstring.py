class Solution(object):
    #condition satisfy ho gya->next case
    #condition satisfy nhi hua->further movement-no next case>till end  nhi hua>>previous i val return
    def lengthOfLongestSubstring(self, s):
        if s=="":
            return 0
        elif len(s)==1:
            return 1
        for i in range(len(s)):#i+1 as count
            for j in range(len(s)-i):
                k=j+i
                dict={}
                count=0
                lcase=0
                if j==len(s)-i-1:
                    lcase=1
                for l in range(j,k+1):
                    if s[l] in dict:
                        break
                    else:
                        dict[s[l]]=1
                        count+=1 
                if count==k+1-j:
                    if i==len(s)-1:
                        return i+1 
                    break    
                if lcase==1:
                    return i  
