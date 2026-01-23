# Last updated: 1/23/2026, 5:58:05 PM
1class Solution:
2    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
3        n = len(nums)
4        ans=[]
5        nums.sort()
6        for i in range(n):
7            if i>0 and nums[i]==nums[i-1]:
8                continue
9            for j in range(i+1,n):
10                if j>i+1 and nums[j]==nums[j-1]:
11                    continue
12                L,R=j+1,n-1
13                while L<R:
14                    summ = nums[i]+nums[j]+nums[L]+nums[R]
15                    if summ==target:
16                        ans.append([nums[i],nums[j],nums[L],nums[R]])
17                        L+=1
18                        R-=1
19                        while L<R and nums[L]==nums[L-1]:
20                            L+=1
21                        while L<R and nums[R]==nums[R+1]:
22                            R-=1
23                    elif summ>target:
24                        R-=1
25                    else:
26                        L+=1
27        return ans