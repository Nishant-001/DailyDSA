
class Solution:
    def findMinOpeartion(self, matrix, n):
        # Code here
        r = [0]*n
        c = [0]*n
        maxe=0
        for i in range(n):
            for j in range(n):
                r[i]+=matrix[i][j]
                maxe=max(maxe,r[i])
                
                c[j] += matrix[i][j];
                maxe = max(maxe, c[j])
                
        
        res =0
        for i in range(n):
            c[i]=maxe-c[i]
            res+=c[i]
            
        return res