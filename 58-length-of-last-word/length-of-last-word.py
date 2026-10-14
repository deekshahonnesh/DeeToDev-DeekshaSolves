class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k=s.split()
        n=len(k)
        j=len(k[n-1])
        return j
        