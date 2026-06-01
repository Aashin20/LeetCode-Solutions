# Last updated: 6/1/2026, 9:53:10 PM
1class Solution:
2    def minimumCost(self, cost: List[int]) -> int:
3        cost.sort(reverse=True)
4        total=0
5        for i, x in enumerate(cost, start=1):
6            if i % 3 == 0:
7                continue
8            total+=x
9        return total