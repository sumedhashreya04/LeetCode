#Time Limit Exceeded
#NTI
class Solution(object):
    def dailyTemperatures(self, temperatures):
        stacki=[]
        temp=[0]*len(temperatures)
        for i in range(len(temperatures)):
            if len(stacki)==0:
                stacki.append([temperatures[i],0,i])
            elif stacki[len(stacki)-1][0]>=temperatures[i]:
                stacki.append([temperatures[i],0,i])
                t=1
                while t!=len(stacki):
                    stacki[len(stacki)-t-1][1]+=1
                    t+=1
            else:
                t=0
                while t!=len(stacki):
                    stacki[len(stacki)-t-1][1]+=1
                    t+=1
                while len(stacki)!=0 and ((temperatures[i])>(stacki[len(stacki)-1][0])):
                    temp[stacki[len(stacki)-1][2]]=stacki[len(stacki)-1][1]
                    stacki.pop()   
                stacki.append([temperatures[i],0,i])
        return temp
