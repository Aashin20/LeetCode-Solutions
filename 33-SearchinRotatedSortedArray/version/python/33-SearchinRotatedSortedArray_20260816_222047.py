# Last updated: 8/16/2026, 10:20:47 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> int:
3        L=0
4        R=len(nums)-1
5        while L<=R:
6            M=(L+R)//2
7            if nums[M]==target:
8                return M
9            elif nums[L]<=nums[M]:
10                if nums[L]<=target<nums[M]:
11                    R=M-1
12                else:
13                    L=M+1
14            else: 
15                if nums[M]<target<=nums[R]:
16                    L=M+1
17                else:
18                    R=M-1
19        return -1