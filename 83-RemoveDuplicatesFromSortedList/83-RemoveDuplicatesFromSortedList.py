# Last updated: 6/14/2025, 10:34:00 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        while ptr and ptr.next:
            if ptr.val==ptr.next.val:
                ptr.next=ptr.next.next
            else:
                ptr=ptr.next
        return head
