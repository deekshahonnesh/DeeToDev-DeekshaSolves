class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        dict1={}
        l=0
        len=0
        for i,j in enumerate(s):
            if j in dict1 and dict1[j]>=l:
                l=dict1[j]+1
            dict1[j]=i
            len1=max(len,i-l+1)
            len=len1
        return len


        

        