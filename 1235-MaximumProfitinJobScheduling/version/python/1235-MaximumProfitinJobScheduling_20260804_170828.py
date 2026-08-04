# Last updated: 8/4/2026, 5:08:28 PM
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
14            # j=binary_search(L,intervals[i][1])
15            j=bisect.bisect(intervals,(intervals[i][1],-1,-1))
16            res=max(res,intervals[i][2]+dfs(j))
17            memo[i]=res
18            return res
19        # def binary_search(L,target):
20        #     R=len(intervals)-1
21        #     ans=len(intervals)
22        #     while L<=R:
23        #         M=(L+R)//2
24        #         if intervals[M][0]>=target:
25        #             ans=M
26        #             R=M-1
27        #         else:
28        #             L=M+1
29        #     return ans
30        return dfs(0)