# Last updated: 1/14/2026, 1:13:55 PM
1class Solution:
2    def threeSum(self, nums: List[int]) -> List[List[int]]:
3        nums.sort()
4        n = len(nums)
5        ans = []
6        for i in range(n):
7            if nums[i]>0:
8                break
9            elif i>0 and nums[i]==nums[i-1]:
10                continue
11            l,r = i+1, n-1
12            while l<r:
13                summ = nums[i]+nums[l]+nums[r]
14                if summ == 0:
15                    ans.append([nums[i],nums[l],nums[r]])
16                    l+=1
17                    r-=1
18                    while l<r and nums[l]==nums[l-1]:
19                        l+=1
20                    while l<r and nums[r]==nums[r+1]:
21                        r-=1
22                elif summ<0:
23                    l+=1
24                else:
25                    r-=1
26        return ans