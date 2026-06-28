# Last updated: 6/28/2026, 6:32:50 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        pre=1
4        pos=1
5        L=[0]*len(nums)
6        R=[0]*len(nums)
7        ans=[0]*len(nums)
8        for i in range(len(nums)):
9            L[i]=pre
10            pre*=nums[i]
11        for i in range(len(nums)-1,-1,-1):
12            R[i]=pos
13            pos*=nums[i]
14        for i in range(len(nums)):
15            ans[i]=L[i]*R[i]
16        return ans