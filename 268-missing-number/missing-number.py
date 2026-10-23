class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
    
    
        for i in range(0,n+1):
            if i in nums:
               continue
            else:
               return i
        