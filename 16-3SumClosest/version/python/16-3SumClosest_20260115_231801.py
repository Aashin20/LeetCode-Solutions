# Last updated: 1/15/2026, 11:18:01 PM
1class Solution:
2    def threeSumClosest(self, nums: List[int], target: int) -> int:
3        nums.sort()
4        n = len(nums)
5        closest = float('inf')
6        for i in range(n):
7            l,r = i+1, n-1
8            while l<r:
9                cur_sum = nums[i]+nums[l]+nums[r]
10                if abs(cur_sum-target)<abs(closest-target):
11                    closest = cur_sum
12                if cur_sum==target:
13                    return cur_sum
14                elif cur_sum<target:
15                    l+=1
16                else:
17                    r-=1
18        return closest