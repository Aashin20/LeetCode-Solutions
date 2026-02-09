# Last updated: 2/9/2026, 7:00:56 PM
1class Solution:
2    def deleteAndEarn(self, nums: List[int]) -> int:
3        count = Counter(nums)
4        nums = sorted(list(set(nums)))
5        prev,cur = 0,0
6        for i in range(len(nums)):
7            earn = nums[i]*count[nums[i]]
8            if i>0 and nums[i]==nums[i-1]+1:
9                temp = cur
10                cur = max(cur,prev+earn)
11                prev = temp
12            else:
13                temp = cur
14                cur = cur+earn
15                prev = temp
16        return cur