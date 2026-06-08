# Last updated: 6/8/2026, 3:04:40 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        if not head: return
9        d=ListNode(0)
10        d.next=head
11        slow=fast=d
12        for i in range(n):
13                fast=fast.next
14        while fast and fast.next:
15            slow=slow.next
16            fast=fast.next
17        slow.next=slow.next.next
18        return d.next