# Last updated: 6/8/2026, 12:41:37 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9        if not head:
10            return
11        visited=set()
12        ptr=head
13        while ptr.next:
14            if ptr.next in visited:
15                return True
16            else:
17                visited.add(ptr.next)
18                ptr=ptr.next
19        return False