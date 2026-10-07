class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n=sorted(nums1+nums2)
        k=len(n)
        if k%2!=0:
            z=(k+1)//2
            return n[z-1]
    
    
        else:
            p1=k//2-1
            p2=k//2
            return((n[p1]+n[p2])/2)

        