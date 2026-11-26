class Solution:
    def countBits(self, n: int) -> list[int]:
        l=[]
        if n==0:
            l.append(0)
            return l
        l.append(0)
        l.append(1)
        for i in range(2,n+1):
            k=[]
            while i//2!=0:
                j=i%2
                k.append(j)
                i=i//2
            k.append(1)
            l.append(k.count(1))
        return l
        