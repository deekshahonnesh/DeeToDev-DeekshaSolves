class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1={}
        
        for i in s:
            if i not in dict1:
               dict1[i]=1
            else:
               dict1[i]+=1
        for k,v in dict1.items():
            if v==1:
               j=s.index(k)
               return j
                
        return -1
        