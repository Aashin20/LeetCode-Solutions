# Last updated: 9/18/2026, 12:43:48 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reorderList(self, head: Optional[ListNode]) -> None:
8        """
9        Do not return anything, modify head in-place instead.
10        """
11        slow,fast=head,head.next
12        while fast and fast.next:
13            fast=fast.next.next
14            slow=slow.next
15        second=slow.next
16        slow.next=None
17        prev=None
18        while second:
19            temp=second.next
20            second.next=prev
21            prev=second
22            second=temp
23        first,second=head,prev
24        while second:
25            tmp1,tmp2=first.next,second.next
26            first.next=second
27            second.next=tmp1
28            first=tmp1
29            second=tmp2
30
31    