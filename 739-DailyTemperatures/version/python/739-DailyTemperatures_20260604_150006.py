# Last updated: 6/4/2026, 3:00:06 PM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        stk=[]
4        n=len(temperatures)
5        ans=[0]*n
6
7        for i in range(n):
8            while stk and temperatures[stk[-1]]<temperatures[i]:
9                index=stk.pop()
10                ans[index]=i-index
11            stk.append(i)
12        return ans