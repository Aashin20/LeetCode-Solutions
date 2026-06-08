# Last updated: 6/8/2026, 12:38:02 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        d=ListNode()
9        cur=d
10        while list1 and list2:
11            if list1.val<list2.val:
12                cur.next=list1
13                cur=list1
14                list1=list1.next
15            else:
16                cur.next=list2
17                cur=list2
18                list2=list2.next
19        cur.next=list1 if list1 else list2
20        return d.next
21
22