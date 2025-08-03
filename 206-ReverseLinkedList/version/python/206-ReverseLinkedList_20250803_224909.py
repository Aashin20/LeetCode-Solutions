# Last updated: 8/3/2025, 10:49:09 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        c=head
        p=None
        while c:
            t=c.next
            c.next=p
            p=c
            c=t
        return p
            
