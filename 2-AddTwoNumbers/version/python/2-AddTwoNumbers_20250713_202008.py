# Last updated: 7/13/2025, 8:20:08 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sett=set()
        curr=head
        while curr:
            if curr in sett:
                return True
            else:
                sett.add(curr)
                curr=curr.next if curr.next else None
        return False