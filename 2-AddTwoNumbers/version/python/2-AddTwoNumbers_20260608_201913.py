# Last updated: 6/8/2026, 8:19:13 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        d=ListNode()
9        cur=d
10        carry=0
11        while l1 or l2 or carry:
12            v1=l1.val if l1 else 0
13            v2=l2.val if l2 else 0
14            summ=v1+v2+carry
15            carry=summ//10
16            val=summ%10
17            cur.next=ListNode(val)
18            cur=cur.next
19            l1=l1.next if l1 else None
20            l2=l2.next if l2 else None
21        return d.next