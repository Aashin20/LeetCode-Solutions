# Last updated: 8/4/2026, 5:06:55 PM
1class Solution:
2    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
3        intervals=sorted(zip(startTime,endTime,profit))
4        memo={}
5        def dfs(i):
6            if i==len(intervals):
7                return 0
8            if i in memo:
9                return memo[i]
10            #Do not include
11            res=dfs(i+1)
12            #Include
13            L=i+1
14            j=binary_search(L,intervals[i][1])
15            res=max(res,intervals[i][2]+dfs(j))
16            memo[i]=res
17            return res
18        def binary_search(L,target):
19            R=len(intervals)-1
20            ans=len(intervals)
21            while L<=R:
22                M=(L+R)//2
23                if intervals[M][0]>=target:
24                    ans=M
25                    R=M-1
26                else:
27                    L=M+1
28            return ans
29        return dfs(0)