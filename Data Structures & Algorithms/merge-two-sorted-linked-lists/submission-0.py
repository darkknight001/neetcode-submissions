# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = list1
        n2 = list2
        n3 = ListNode(-101)
        head = n3
        while(n1 and n2):
            if n1.val<=n2.val:
                n3.next = n1
                n1 = n1.next
            else:
                n3.next = n2
                n2 = n2.next
            n3 = n3.next
    
        while(n1):
            n3.next = n1
            n1 = n1.next
            n3 = n3.next
        
        while(n2):
            n3.next = n2
            n2 = n2.next
            n3 = n3.next
        
        return head.next

