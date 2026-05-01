# Last updated: 5/1/2026, 11:35:04 PM
1class Solution:
2    def searchInsert(self, nums: List[int], target: int) -> int:
3        l=0
4        r=len(nums)-1
5        while l<=r:
6            mid=(l+r)//2
7            if nums[mid]==target:
8                return mid
9            elif nums[mid]<target:
10                l=mid+1
11            else:
12                r=mid-1
13        return l