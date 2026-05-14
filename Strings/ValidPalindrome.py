# Problem: Valid Palindrome
# Platform: LeetCode
# Difficulty: Easy
class Solution(object):
    def isPalindrome(self, s):
        st=[]
        i=0
        for t in s:
            idx=ord(t)
            if ((65<=idx<=90) or (97<=idx<=122)or(48<=idx<=57)):
                if (65<=idx<=90):
                    idx+=32
                st.insert(i,idx)
                i+=1
        j=0
        if len(st)%2==0:
            b=len(st)/2
        else:
            b=(len(st)-1)/2
        for i in range(0,(b)):
            if st[i]==st[len(st)-1-i] :
                j+=1
        if j==b :
            return True
        else:
            return False

"""
Time Complexity: O(n)
Space Complexity: O(1)

Learned:
-Brute force logic implementation
-Optimization
"""
