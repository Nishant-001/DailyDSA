class Solution
{
    public boolean isValid(int[][] matrix,int i,int j){
        int n=matrix.length;
        int m=matrix[i].length;
        int c=0;
        //top
        if(i-1>=0 && matrix[i-1][j]==0)c++;
        //down
        if(i+1<n  && matrix[i+1][j]==0)c++;
        //left
        if(j-1>=0 && matrix[i][j-1]==0)c++;
        //right
        if( j+1<m && matrix[i][j+1]==0)c++;
        //up-left
        if(i-1>=0 && j-1>=0 && matrix[i-1][j-1]==0)c++;
        //up=right
         if(i-1>=0 && j+1<m && matrix[i-1][j+1]==0)c++;
        //left-down
         if(i+1<n && j-1>=0 && matrix[i+1][j-1]==0)c++;
        //right-down
         if(i+1<n && j+1<m  && matrix[i+1][j+1]==0)c++;
         
         
         if(c>0 && c%2==0)return true;
         else return false;
    }
    public int  Count(int[][] matrix)
    {
        int count=0;
        for(int i=0;i<matrix.length;i++){
            for(int j=0;j<matrix[0].length;j++){
                if( matrix[i][j]==1 && isValid(matrix,i,j))
                count++;
            }
            
        }
        return count;
    }
}