class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        stack=[]
        for i in nums1[:m]:
            if i==0:
               continue
            else:
               stack.append(i)
        for j in nums2[:n]:
            if j==0:
                continue
            else:
                stack.append(j)
        while len(stack) < (m + n):
            stack.append(0)
    

        stack.sort()
        nums1[:]=stack
        
        