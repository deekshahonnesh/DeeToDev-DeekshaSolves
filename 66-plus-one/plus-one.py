class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        c=""
        for i in digits:
            k=str(i)
            m=c+k
            c=m
        j=int(c)+1
        p=str(j)
        l=[]
        for h in p:
            l.append(int(h))
        return l
            

        
        
        