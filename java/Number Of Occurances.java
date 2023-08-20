class Solution {
    int count(int[] arr, int n, int x) {
        // code here
        int minx=0,max=0;
        int lo=0,hi=n-1;
        while(lo<=hi)
        {
            int mid=(lo+hi)/2;
            if(arr[mid]>=x)
            {
                hi=mid-1;
            }
            else
            {
                lo=mid+1;
            }
        }
        minx=lo;
        lo=0;hi=n-1;
        while(lo<=hi)
        {
            int mid=(lo+hi)/2;
            if(arr[mid]>x)
            {
                hi=mid-1;
            }
            else
            {
                lo=mid+1;
            }
        }
        max=lo;
        // System.out.println(minx+"-"+max);
        return max-minx;
    }
}