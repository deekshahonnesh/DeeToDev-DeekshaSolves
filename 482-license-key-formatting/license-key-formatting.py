class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        m=s.upper()
        j=m.split("-")
        n="".join(j)
        t=[]
        for i in range(-1,-len(n)-1,-k):
            t.append(n[i:i-k:-1][::-1])
        t.reverse()
        return "-" .join(t) 
        