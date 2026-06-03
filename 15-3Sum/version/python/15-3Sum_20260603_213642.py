# Last updated: 6/3/2026, 9:36:42 PM
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        nums.sort()
4        ans=[]
5        n=len(nums)
6        for i in range(n):
7            if nums[i]>0: break
8            elif i>0 and nums[i]==nums[i-1]: continue
9            k=nums[i]
10            L=i+1
11            R=n-1
12            while L<R:
13                summ=nums[L]+nums[R]+nums[i]
14                if summ==0:
15                    ans.append([k,nums[L],nums[R]])
16                    L+=1
17                    R-=1
18                    while L<R and nums[L]==nums[L-1]: L+=1
19                    while L<R and nums[R]==nums[R+1]: R-=1
20                elif summ>0: R-=1
21                else: L+=1
22        return ans
23