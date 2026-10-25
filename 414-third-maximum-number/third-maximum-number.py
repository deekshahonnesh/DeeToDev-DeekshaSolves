class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums.sort(reverse=True)
        dict={}
    
        for i in nums:
           if i  not in dict:
              dict[i]=1
           else:
              dict[i]+=1
        if len(dict)>=3:
           return list(dict.keys())[2] 
        else:
           return list(dict.keys())[0]
        