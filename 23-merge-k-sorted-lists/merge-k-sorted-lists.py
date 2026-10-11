# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        arr = []
        
        # 1. Extract all values into a standard Python list
        for head in lists:
            current = head
            while current is not None:
                arr.append(current.val)
                current = current.next
        
        # 2. Sort the array
        arr.sort()
        
        # 3. Use your dummy and tail logic to build the final list!
        dummy = ListNode(-1)
        tail = dummy
        
        for val in arr:
            tail.next = ListNode(val)
            tail = tail.next
            
        return dummy.next

        