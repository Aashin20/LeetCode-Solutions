# Last updated: 6/6/2026, 8:26:31 PM
1class Solution:
2    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
3        if not intervals:
4            return 0
5        intervals.sort()
6        time=0
7        s,e = intervals[0]
8        for ns,ne in intervals[1:]:
9            if ns<=e+1:
10                e=max(e,ne)
11            else:
12                time+=e-s+1
13                s,e=ns,ne
14        time+=e-s+1
15        bulbs=(brightness+2)//3
16        return bulbs*time