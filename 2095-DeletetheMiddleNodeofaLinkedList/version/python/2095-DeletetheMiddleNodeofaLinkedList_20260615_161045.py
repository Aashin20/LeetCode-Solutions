# Last updated: 6/15/2026, 4:10:45 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        d=ListNode()
9        d.next=head
10        fast=slow=head
11        prev=d
12        while fast and fast.next:
13            fast=fast.next.next
14            slow=slow.next
15            prev=prev.next
16        prev.next=slow.next
17        return d.next
18
19        