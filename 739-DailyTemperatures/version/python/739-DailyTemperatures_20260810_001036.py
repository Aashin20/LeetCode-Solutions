# Last updated: 8/10/2026, 12:10:36 AM
1class Solution:
2    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
3        stk=[]
4        n=len(temperatures)
5        ans=[0]*n
6        for i in range(len(temperatures)):
7            while stk and temperatures[stk[-1]]<temperatures[i]:
8                idx=stk.pop()
9                ans[idx]=i-idx
10            stk.append(i)
11        return ans