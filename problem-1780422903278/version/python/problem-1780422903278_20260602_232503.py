# Last updated: 6/2/2026, 11:25:03 PM
1class Solution:
2    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
3        def solve(st1,dr1,st2,dr2):
4            finish1=inf
5            for i in range(len(st1)):
6                finish1=min(finish1,st1[i]+dr1[i])
7            finish2=inf
8            for i in range(len(st2)):
9                finish2=min(finish2,max(finish1,st2[i])+dr2[i])
10            return finish2
11        land=solve(landStartTime,landDuration,waterStartTime,waterDuration)
12        water=solve(waterStartTime,waterDuration,landStartTime,landDuration)
13        return min(land,water)