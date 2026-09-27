# Last updated: 9/27/2026, 12:35:17 PM
1class Solution:
2    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
3        ans=[]
4        for i in nums1:
5            if i in nums2:
6                ans.append(i)
7                nums2.remove(i)
8        return ans