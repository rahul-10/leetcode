class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(0, math.floor(n/2)):
            for j in range(0, n):
                matrix[i][j], matrix[n-1-i][j] =  matrix[n-1-i][j], matrix[i][j]
            
        for i in range(1, n):
            for j in range(0, i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]