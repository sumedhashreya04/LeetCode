#Search a 2D Matrix
class Solution(object):
    def searchMatrix(self, matrix, target):
        st=0
        end=len(matrix)-1
        while st<end:
            mid=int((st+end)/2)
            if matrix[mid][0]>target:
                end=mid-1
            elif matrix[mid][0]<target:
                st=mid+1
            else:
                return True
        if end==st:
            if matrix[st][0]>target:
                row=st-1
            elif matrix[st][0]<target:
                row=st
            else:
                return True
        else:
            row=end
        
        st=0
        end=len(matrix[0])-1
        while st<=end:
            mid=int((st+end)/2)
            if matrix[row][mid]>target:
                end=mid-1
            elif matrix[row][mid]<target:
                st=mid+1
            else:
                return True
        return False
