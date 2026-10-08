class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        n=len(nums)
        for i,j in enumerate (nums): 
            if j==target:
               return i
            elif j>target:
             
        
                return i
        return n 

        