# Last updated: 6/14/2025, 10:34:19 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        a=b=dummy
        for i in range(n+1):
            a=a.next
        while a:
            a=a.next
            b=b.next
        b.next=b.next.next
        return dummy.next

        
        