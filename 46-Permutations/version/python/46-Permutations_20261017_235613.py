# Last updated: 10/17/2026, 11:56:13 PM
1class Solution:
2    def permute(self, nums: list[int]) -> list[list[int]]:
3        res,sol=[],[]
4        n=len(nums)
5        def backtrack():
6            if len(sol)==n:
7                res.append(sol[:])
8                return
9            for i in nums:
10                if i not in sol:
11                    sol.append(i)
12                    backtrack()
13                    sol.pop()
14        backtrack()
15        return res