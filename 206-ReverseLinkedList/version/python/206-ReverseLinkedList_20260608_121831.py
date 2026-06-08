# Last updated: 6/8/2026, 12:18:31 PM
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
13            temp=cur.next
14            cur.next=prev
15            prev=cur
16            cur=temp
17        return prev
18
19
20