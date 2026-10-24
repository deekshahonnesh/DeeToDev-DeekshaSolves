class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        for i in nums:
           k=nums.count(i)
           if k==1:
              return i
        