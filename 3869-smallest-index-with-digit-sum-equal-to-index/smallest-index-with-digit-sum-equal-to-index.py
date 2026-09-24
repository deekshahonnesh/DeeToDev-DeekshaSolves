class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        list=[]
        for num in nums:
            
            t=sum(int(char) for char in str(num))
            list.append(t)
        for i,n in enumerate(list):
            if i==n:
                return i
        return -1
        