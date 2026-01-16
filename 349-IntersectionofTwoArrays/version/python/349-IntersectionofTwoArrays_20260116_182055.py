# Last updated: 1/16/2026, 6:20:55 PM
1class Solution:
2    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        nums=set(nums1)
4        ans=[]
5        for i in nums2:
6            if i in nums:
7                ans.append(i)
8                nums.remove(i)
9        return ans