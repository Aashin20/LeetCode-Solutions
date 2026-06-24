# Last updated: 6/24/2026, 9:36:22 PM
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        nums.sort()
4        ans=[]
5        n=len(nums)
6        for i in range(n):
7            if nums[i]>0: break
8            elif i>0 and nums[i]==nums[i-1]: continue
9            L=i+1
10            R=n-1
11            while L<R:
12                summ=nums[L]+nums[R]+nums[i]
13                if summ==0:
14                    ans.append([nums[i],nums[L],nums[R]])
15                    L+=1
16                    R-=1
17                    while L<R and nums[L]==nums[L-1]: L+=1
18                    while L<R and nums[R]==nums[R+1]: R-=1
19                elif summ>0: R-=1
20                else: L+=1
21        return ans
22