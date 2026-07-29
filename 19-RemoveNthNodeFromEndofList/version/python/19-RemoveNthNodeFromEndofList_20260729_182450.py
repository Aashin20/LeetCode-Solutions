# Last updated: 7/29/2026, 6:24:50 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        if not head:
9            return None
10        d=ListNode(0)
11        d.next=head
12        slow=fast=d
13        for i in range(n):
14            fast=fast.next
15        while fast and fast.next:
16            slow=slow.next
17            fast=fast.next
18        slow.next=slow.next.next
19        return d.next