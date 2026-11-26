class Solution:
    def countBits(self, n: int) -> list[int]:
        l=[]
        
        for i in range(0,n+1):
            k=[]
            while i//2!=0:
                j=i%2
                k.append(j)
                i=i//2
            k.append(i)
            l.append(k.count(1))
        return l
        