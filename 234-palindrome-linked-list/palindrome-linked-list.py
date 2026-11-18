# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        arr=[]
        while head is not None:
             arr.append(head.val)
             head=head.next
        def palidrome(i,j):
            if i>j:
               return True
            elif arr[i]!=arr[j]:
               return False
            return palidrome(i+1,j-1)
            
        return palidrome(0,len(arr)-1)

        
        