# Last updated: 2/15/2026, 11:20:42 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
8        dummy = ListNode()
9        curr = dummy
10        carry = 0
11
12        while l1 or l2 or carry:
13            v1 = l1.val if l1 else 0
14            v2 = l2.val if l2 else 0
15
16            sum = v1+v2+carry
17            carry = sum//10
18            sum = sum%10
19
20            curr.next = ListNode(sum)
21
22            curr = curr.next
23            l1 = l1.next if l1 else None
24            l2 = l2.next if l2 else None
25
26        return dummy.next