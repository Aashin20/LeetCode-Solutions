# Last updated: 3/11/2026, 8:52:43 PM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        res = []
4        intervals.sort(key = lambda interval: interval[0])
5        for i in intervals:
6            if not res or res[-1][1]<i[0]:
7                res.append(i)
8            else:
9                res[-1] = [res[-1][0],max(res[-1][1],i[1])]
10        return res