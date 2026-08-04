# Last updated: 8/4/2026, 5:42:54 PM
1class Solution:
2    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
3        rides=sorted(rides)
4        memo={}
5        def dfs(i):
6            if i==len(rides): return 0
7            if i in memo: return memo[i]
8            res=dfs(i+1)
9            j=binary_search(i+1,rides[i][1])
10            res=max(res,(rides[i][1]-rides[i][0])+rides[i][2]+dfs(j))
11            memo[i]=res
12            return res
13        
14
15        def binary_search(L,target):
16            R=len(rides)-1
17            ans=len(rides)
18            while L<=R:
19                M=(L+R)//2
20                if rides[M][0]>=target:
21                    ans=M
22                    R=M-1
23                else:
24                    L=M+1
25            return ans
26        return dfs(0)