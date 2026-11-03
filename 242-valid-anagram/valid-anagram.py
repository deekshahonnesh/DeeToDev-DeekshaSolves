class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
           return False
        dict1={}
        dict2={}
        for i,j in zip(s,t):
            if i in dict1:
              dict1[i]+=1
            else:
              dict1[i]=1
            if j in dict2:
               dict2[j]+=1
            else:
               dict2[j]=1
        if dict1==dict2:
           return True
        else:
           return False
        