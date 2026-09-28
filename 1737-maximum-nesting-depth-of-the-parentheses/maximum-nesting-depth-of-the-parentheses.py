class Solution:
    def maxDepth(self, s: str) -> int:
        maxd=0
        c=0
        for char in s :
            if char=="(":
               c+=1
            if c>maxd:
                    maxd=c
            elif char==")":
                c-=1
        return maxd
        