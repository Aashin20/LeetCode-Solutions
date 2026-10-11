# Last updated: 10/11/2026, 11:31:53 PM
1class Solution:
2    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
3        res,sol=[],[]
4        n=len(candidates)
5        candidates.sort()
6        def backtrack(i,cur):
7            if cur==target:
8                res.append(sol[:])
9                return
10            if i==n or cur>target:
11                return
12            sol.append(candidates[i])
13            backtrack(i+1,cur+candidates[i])
14            sol.pop()
15            while i+1<n and candidates[i]==candidates[i+1]:
16                i+=1
17            backtrack(i+1,cur)
18            
19        backtrack(0,0)
20        return res
21            