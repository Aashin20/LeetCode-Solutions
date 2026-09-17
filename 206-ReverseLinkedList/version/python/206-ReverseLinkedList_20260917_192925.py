# Last updated: 9/17/2026, 7:29:25 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        cur=head
9        prev=None
10        while cur:
11            temp=cur.next
12            cur.next=prev
13            prev=cur
14            cur=temp
15        return prev