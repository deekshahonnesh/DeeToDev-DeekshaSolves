# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        
        # Step 2: Extract all values from the linked list into a Python array
        values = []
        current = head
        while current is not None:
            values.append(current.val)
            current = current.next
        # Step 3: Sort the standard Python array
        values.sort()
        
        # Step 4: Rebuild the sorted node chain using your dummy strategy
        dummy = ListNode(-1)
        tail = dummy
        for num in values:
            tail.next = ListNode(num)
            tail = tail.next
            
        return dummy.next


        