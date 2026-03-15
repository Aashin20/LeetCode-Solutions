# Last updated: 3/15/2026, 11:02:16 PM
1class Solution:
2    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3        res = []
4        for i in range(len(intervals)):
5            if intervals[i][0]>newInterval[1]:
6                res.append(newInterval)
7                return res+intervals[i:]
8            elif intervals[i][1]<newInterval[0]:
9                res.append(intervals[i])
10            else:
11                newInterval = [min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])]
12        res.append(newInterval)
13        return res