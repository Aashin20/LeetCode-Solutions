# Last updated: 7/29/2026, 5:05:57 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        if not head:
9            return 
10        cur=head
11        prev=None
12        while cur:
13            tmp=cur.next
14            cur.next=prev
15            prev=cur
16            cur=tmp
17        return prev
18