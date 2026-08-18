# Last updated: 8/18/2026, 11:33:35 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        dummy=ListNode(0)
9        d=dummy
10        while list1 and list2:
11            if list1.val<=list2.val:
12                dummy.next=list1
13                list1=list1.next
14            else:
15                dummy.next=list2
16                list2=list2.next
17            dummy=dummy.next
18        if list1:
19            dummy.next=list1
20        elif list2: 
21            dummy.next=list2
22        return d.next