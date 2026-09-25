class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
            n=len(nums)
            dict={}
            i=0
            for num in nums:
                dict[num]=i
                i=i+1
            list1=list(dict)
            uni=len(list1)
            while len(list1)!=n:
                list1.append("_")
                nums[:]=list1
                

            return uni

        