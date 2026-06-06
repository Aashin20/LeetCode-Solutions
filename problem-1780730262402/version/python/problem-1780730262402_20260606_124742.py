# Last updated: 6/6/2026, 12:47:42 PM
1class Solution:
2    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
3        pair=[[p,s] for p,s in zip(position,speed)]
4        stk=[]
5
6        for p,s in sorted(pair)[::-1]:
7            stk.append((target-p)/s)
8            if len(stk)>=2 and stk[-1]<=stk[-2]:
9                stk.pop()
10        return len(stk)