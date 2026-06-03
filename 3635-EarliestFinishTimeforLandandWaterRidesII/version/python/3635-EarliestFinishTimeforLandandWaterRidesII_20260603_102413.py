# Last updated: 6/3/2026, 10:24:13 AM
1class Solution:
2    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
3        def solve(st1,dr1,st2,dr2):
4            finish1=inf
5            for i in range(len(st1)):
6                finish1=min(finish1,st1[i]+dr1[i])
7            
8            finish2 = inf
9
10            for i in range(len(st2)):
11                finish2=min(finish2,max(finish1,st2[i])+dr2[i])
12            return finish2
13
14        landRides = solve(landStartTime,landDuration,waterStartTime,waterDuration)
15        waterRides = solve(waterStartTime,waterDuration,landStartTime,landDuration)
16        return min(landRides,waterRides)