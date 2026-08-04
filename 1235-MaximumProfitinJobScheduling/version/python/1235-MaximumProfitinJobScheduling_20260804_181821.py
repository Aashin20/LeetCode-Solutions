# Last updated: 8/4/2026, 6:18:21 PM
1class Solution:
2    def maxValue(self, events: List[List[int]], k: int) -> int:
3        events.sort()
4        memo={}
5        res=0
6        def dfs(i,k):
7            if i==len(events): return 0
8            if k==0: return 0
9            if (i,k) in memo: return memo[(i,k)]
10            res=dfs(i+1,k)
11            j=binary_search(i+1,events[i][1])
12            res=max(res,events[i][2]+dfs(j,k-1))
13            memo[(i,k)]=res
14            return res
15        
16        def binary_search(L,target):
17            R=len(events)-1
18            ans=len(events)
19            while L<=R:
20                M=(L+R)//2
21                if events[M][0]>target:
22                    ans=M
23                    R=M-1
24                else:
25                    L=M+1
26            return ans
27        return dfs(0,k)