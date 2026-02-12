# Last updated: 2/12/2026, 8:45:53 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        l = 0
4        r = len(nums)-1
5        while l<=r:
6            m = (l+r)//2
7            if nums[m] == target:
8                return m
9            elif nums[m]<target:
10                l = m+1
11            else:
12                r = m-1
13        return -1