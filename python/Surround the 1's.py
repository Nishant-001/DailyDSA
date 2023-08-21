class Solution:
    def is_valid(self,matrix, i, j):
        n = len(matrix)
        m = len(matrix[i])
        c = 0
        
        # top
        if i - 1 >= 0 and matrix[i - 1][j] == 0:
            c += 1
        # down
        if i + 1 < n and matrix[i + 1][j] == 0:
            c += 1
        # left
        if j - 1 >= 0 and matrix[i][j - 1] == 0:
            c += 1
        # right
        if j + 1 < m and matrix[i][j + 1] == 0:
            c += 1
        # up-left
        if i - 1 >= 0 and j - 1 >= 0 and matrix[i - 1][j - 1] == 0:
            c += 1
        # up-right
        if i - 1 >= 0 and j + 1 < m and matrix[i - 1][j + 1] == 0:
            c += 1
        # left-down
        if i + 1 < n and j - 1 >= 0 and matrix[i + 1][j - 1] == 0:
            c += 1
        # right-down
        if i + 1 < n and j + 1 < m and matrix[i + 1][j + 1] == 0:
            c += 1
            
        return c > 0 and c % 2 == 0
    
    def Count(self,matrix):
        count = 0
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1 and self.is_valid(matrix, i, j):
                    count += 1
        return count