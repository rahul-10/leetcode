class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix) # row
        n = len(matrix[0]) # columm

        is_raw_has_zero = False
        is_column_has_zero = False
        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

                if matrix[i][j] == 0 and i == 0:
                    is_raw_has_zero = True

                if matrix[i][j] == 0 and j == 0:
                    is_column_has_zero = True

        # update rows
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0
        # print('matrix: ', matrix)

        # update columns
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0
        # print('matrix: ', matrix)

        if is_raw_has_zero:
            for j in range(0, n):
                matrix[0][j] = 0
        
        if is_column_has_zero:
            for i in range(0, m):
                    matrix[i][0] = 0
        
