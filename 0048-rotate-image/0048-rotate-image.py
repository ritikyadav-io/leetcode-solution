class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)

        for i in range(n): #Transpose
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        for row in matrix: #reverse rows 
            left = 0 
            right = n-1

            while left<right:
                row[left], row[right] = row[right], row[left]
                left+=1
                right-=1        