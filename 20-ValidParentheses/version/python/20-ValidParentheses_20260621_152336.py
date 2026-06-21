# Last updated: 6/21/2026, 3:23:36 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        stk=[]
4        s=list(s)
5        hashmap={')':'(',']':'[','}':'{'}
6        for i in s:
7            if i not in hashmap: stk.append(i)
8            else:
9                if not stk: return False
10                top=stk.pop()
11                if top!=hashmap[i]: return False
12        return not stk