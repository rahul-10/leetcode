class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res: Lint[int] = []
        m = len(matrix)
        n = len(matrix[0])

        diff = 1
        i = -1
        j = -1        
        print('m/2: ', m/2)
        while i < m/2:
            i = j = diff -1
            print('i : ', i, ', j: ', j )
            # increase column
            is_itirated = False
            while j <= n-diff:
                res.append(matrix[i][j])
                j = j+1
                is_itirated = True
            
            if not is_itirated:
                break

            i  = i+1
            j = j-1
                
            is_itirated = False
            # increase row
            while i <= m-diff:
                res.append(matrix[i][j])
                i = i+1
                is_itirated = True

            if not is_itirated:
                break

            j = j-1
            i = i-1

            is_itirated = False
            # decrease column
            while j >= diff-1 :
                res.append(matrix[i][j])
                j = j-1
                is_itirated = True

            if not is_itirated:
                break

            i  = i-1
            j = j+1

            is_itirated = False
            # decrease row
            while i > diff-1:
                res.append(matrix[i][j])
                i = i-1
            i = i+1
            diff = diff+1
            print('i : ', i )
        
        return res    
            
                