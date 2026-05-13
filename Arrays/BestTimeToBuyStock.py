#BruteForce method
#Time Limit Exceed
#Not that much idea about optimization
#Time Limit Exceeded
#Time Complexity O(n2)
class Solution(object):
    def maxProfit(self, prices):
        max=float('-inf')
        for i in range(0,len(prices)-1):
            for j in range(i,len(prices)):
                diff=prices[j]-prices[i]
                if diff>max :
                    max=diff
        if max<0:
            return 0
        else:
            return max
          
