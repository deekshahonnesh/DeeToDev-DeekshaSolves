class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
       # list1=[]
       # n=len(nums)
       # for i in range(0,n-2):
       #     for j in range(i+1,n-1):
       #         for t in range (j+1,n):
       #            k=nums[i]+nums[j]+nums[t]
       #            if k==0:
       #               p=sorted([nums[i],nums[j],nums[t]])
       #               if p not in list1:
       #          
       #                  list1.append([nums[i],nums[j],nums[t]])
       #                  
       #          
       # return list1
        list1 = []
        nums.sort()  
        n = len(nums)
        
        for i in range(0, n - 2):
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            
            j =i+1
            t = n - 1      
            
            while j < t:
                k = nums[i] + nums[j] + nums[t]
                
                if k == 0:
                     list1.append([nums[i], nums[j], nums[t]])
                    
                    
                     while j < t and nums[j] == nums[j + 1]:
                         j += 1
                     while j < t and nums[t] == nums[t - 1]:
                         t -= 1
                        
                     j += 1
                     t -= 1
                elif k < 0:
                          j += 1  
                else:
                         t -= 1  
                    
        return list1
