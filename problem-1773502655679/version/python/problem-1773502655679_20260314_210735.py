# Last updated: 3/14/2026, 9:07:35 PM
1from collections import Counter
2class Solution:
3    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
4        total = Counter(nums1)+Counter(nums2)
5        for v in total.values():
6            if v%2!=0:
7                return -1
8        a = {k:v//2 for k,v in total.items()}
9        nums = Counter(nums1)
10        res = 0
11        for i in a:
12            if nums[i]>a[i]:
13                res+=nums[i]-a[i]
14        return res