# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]

        """
        arr1 = []
        while l1:
            arr1.append(l1.val)
            l1 = l1.next
            
        arr2 = []
        while l2:
            arr2.append(l2.val)
            l2 = l2.next
        str1 = "".join(str(num) for num in arr1[::-1])
        str2 = "".join(str(num) for num in arr2[::-1])
        
        # Add the actual numbers together
        total_sum = int(str1) + int(str2)
        
        # Convert total sum back to a reversed list of integers
        # e.g., 30 becomes '30' -> reversed to '03' -> converted to 
        r = [int(x) for x in str(total_sum)[::-1]]


       

        
        
        dummy = ListNode(0)
        current = dummy
        
        for num in r:
            current.next = ListNode(num)
            current = current.next
            
        return dummy.next

        
            
        



        