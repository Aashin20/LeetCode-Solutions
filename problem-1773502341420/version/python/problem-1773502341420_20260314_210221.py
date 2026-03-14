# Last updated: 3/14/2026, 9:02:21 PM
1import math
2class Solution:
3    def gcdSum(self, nums: list[int]) -> int:
4        res = []
5        maxx = 0
6        for i in range(len(nums)):
7            maxx = max(nums[i],maxx)
8            res.append(math.gcd(maxx,nums[i]))
9        res.sort()
10        l,r = 0,len(res)-1
11        ans = 0
12        while l<r:
13            ans+=math.gcd(res[l],res[r])
14            l+=1
15            r-=1
16        return ans