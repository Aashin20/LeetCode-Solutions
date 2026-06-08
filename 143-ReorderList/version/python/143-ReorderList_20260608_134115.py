# Last updated: 6/8/2026, 1:41:15 PM
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
11        #Finding mid
12        slow,fast=head,head.next
13        while fast and fast.next:
14            slow=slow.next
15            fast=fast.next.next
16        #Reversing
17        second=slow.next
18        prev=slow.next=None
19        while second:
20            tmp=second.next
21            second.next=prev
22            prev=second
23            second=tmp
24        #Merging
25        first,second=head,prev
26        while second:
27            tmp1,tmp2=first.next,second.next
28            first.next=second
29            second.next=tmp1
30            first,second=tmp1,tmp2
31            
32
33