# Last updated: 9/18/2026, 12:50:04 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        d=ListNode(0)
9        d.next=head
10        slow=fast=d
11        for i in range(n):
12            fast=fast.next
13        while fast and fast.next:
14            slow=slow.next
15            fast=fast.next
16        slow.next=slow.next.next
17        return d.next
18        