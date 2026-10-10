# Last updated: 10/10/2026, 11:53:29 PM
1class Solution:
2    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
3        n=len(candidates)
4        res,sol=[],[]
5        
6        def backtrack(i,cur):
7            if cur==target:
8                res.append(sol[:])
9                return
10            if i==n or cur>target:
11                return
12            backtrack(i+1,cur)
13            sol.append(candidates[i])
14            backtrack(i,cur+candidates[i])
15            sol.pop()
16        backtrack(0,0)
17        return res