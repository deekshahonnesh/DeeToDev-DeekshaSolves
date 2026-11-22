class Solution:
    def digitSum(self, s: str, k: int) -> str:
            n=len(s)
            if n<=k:
               return s
            list1=[]
            for i in range(0,n,k):
                p=(s[i:i+k])
        
                list1.append(str(sum([int(t) for t in p])))
            m="".join(list1)
            return self.digitSum(m,k)