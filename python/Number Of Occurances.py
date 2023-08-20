class Solution:

	def count(self,arr, n, x):
		# code here
        lo=0
        hi=n-1
        while lo<=hi:
            mid=(lo+hi) // 2
            if arr[mid]>=x:
                hi=mid-1
            else:
                lo=mid+1
        
        minx=lo
        lo=0
        hi=n-1
        while lo<=hi:
            mid=(lo+hi) // 2
            if arr[mid]>x:
                hi=mid-1
            else:
                lo=mid+1
        max=lo
        
        return (max-minx)