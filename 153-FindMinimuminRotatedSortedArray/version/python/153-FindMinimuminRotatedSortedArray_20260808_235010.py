# Last updated: 8/8/2026, 11:50:10 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        L=0
4        R=len(nums)-1
5        while L<R:
6            M=(L+R)//2
7            if nums[M]>nums[R]:
8                L=M+1
9            else:
10                R=M
11        return nums[L]