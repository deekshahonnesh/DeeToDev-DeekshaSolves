# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        c=0
        dict={}
        while head is not None:
            if head not in dict:
                dict[head.val]=c
                head=head.next
                c+=1
        dummy=ListNode(-1)
        tail=dummy
        for i in dict:
            tail.next=ListNode(i)
            tail=tail.next
        return dummy.next

        