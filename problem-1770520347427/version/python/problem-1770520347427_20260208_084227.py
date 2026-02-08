# Last updated: 2/8/2026, 8:42:27 AM
1class Solution:
2    def mergeAdjacent(self, nums: List[int]) -> List[int]:
3        stk = []
4        for x in nums:
5            stk.append(x)
6            while len(stk)>=2 and stk[-1]==stk[-2]:
7                val=stk.pop()
8                stk[-1]+=val
9        return stk
10                