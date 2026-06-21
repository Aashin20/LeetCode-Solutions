# Last updated: 6/21/2026, 10:44:25 AM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        if not intervals:
4            return []
5        intervals.sort(key=lambda x:x[0])
6        res=[]
7        for i in intervals:
8            if not res or res[-1][1]<i[0]:
9                res.append(i)
10            else:
11                res[-1]=[min(res[-1][0],i[0]),max(res[-1][1],i[1])]
12        return res            
13