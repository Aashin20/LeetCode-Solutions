# Last updated: 9/17/2026, 8:59:57 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        if not head: return False
10        fast=slow=head
11        while fast and fast.next:
12            fast=fast.next.next
13            slow=slow.next
14            if fast==slow:
15                return True
16        return False