# Last updated: 10/9/2026, 10:00:40 PM
1class Solution:
2    def subsets(self, nums: list[int]) -> list[list[int]]:
3        n=len(nums)
4        res,sol=[],[]
5
6        def backtrack(i):
7            if i==n:
8                res.append(sol[:])
9                return 
10            backtrack(i+1)
11            sol.append(nums[i])
12            backtrack(i+1)
13            sol.pop()
14        backtrack(0)
15        return res