# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        
        dummy = ListNode(0)
        
        # 2. 'tail' will track the last node of our newly merged list
        tail = dummy
        
        # 3. Compare values at the front of both lists until one list runs out
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                tail.next = list1      # Link the smaller node from list1
                list1 = list1.next     # Advance the list1 pointer
            else:
                tail.next = list2      # Link the smaller node from list2
                list2 = list2.next     # Advance the list2 pointer
                
            tail = tail.next           # Move the tail forward to the new end
        if list1 is not None:
            tail.next = list1
        else:
            tail.next = list2
            
        # 5. Return the merged list, skipping the dummy anchor node
        return dummy.next
    
            

        