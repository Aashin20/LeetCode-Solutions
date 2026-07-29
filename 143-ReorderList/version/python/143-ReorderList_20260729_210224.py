# Last updated: 7/29/2026, 9:02:24 PM
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
11        slow=fast=head
12        while fast and fast.next:
13            slow=slow.next
14            fast=fast.next.next
15        middle=slow.next
16        prev=slow.next=None
17        while middle:
18            tmp=middle.next
19            middle.next=prev
20            prev=middle
21            middle=tmp
22        first,second=head,prev
23        while first and second:
24            tmp1,tmp2=first.next,second.next
25            first.next=second
26            second.next=tmp1
27            first,second=tmp1,tmp2
28
29
30