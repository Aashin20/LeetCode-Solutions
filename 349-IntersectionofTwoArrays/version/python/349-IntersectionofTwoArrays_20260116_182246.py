# Last updated: 1/16/2026, 6:22:46 PM
1class Solution:
2    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        nums1=set(nums1)
4        nums2=set(nums2)
5        ans=[]
6        for i in nums2:
7            if i in nums1:
8                ans.append(i)
9                nums1.remove(i)
10        return ans