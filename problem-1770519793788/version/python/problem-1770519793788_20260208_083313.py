# Last updated: 2/8/2026, 8:33:13 AM
1class Solution:
2    def dominantIndices(self, nums: List[int]) -> int:
3        n=len(nums)
4        summ=sum(nums)
5        count=0
6        for i in range(n-1):
7            summ-=nums[i]
8            avg = summ/(n-i-1)
9            if nums[i]>avg:
10                count+=1
11        return count
12        