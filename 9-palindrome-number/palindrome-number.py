class Solution:
    def isPalindrome(self, x: int) -> bool:
        list1=str(x)
    
        n=len(list1)
        for i in list1:
            if i==list1[n-1]:
               n=n-1
            else:
                return False
        return True
        