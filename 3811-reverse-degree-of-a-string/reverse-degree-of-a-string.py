class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        lowercase=[chr(x) for x in range(97,123)]
        dict1={}
        j=0
        for i,t in enumerate(lowercase):
           t=26-j
           dict1[lowercase[i]]=t
           j+=1



    
        k=list(s)
        list1=[]
    
        for h,e in enumerate(k):
            if e in dict1:
               b=dict1[e]
               y=b*(h+1)
               list1.append(y)

        
            
        
        
        r=sum(list1)
        return r

        
            
        