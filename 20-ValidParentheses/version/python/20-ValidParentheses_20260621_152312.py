# Last updated: 6/21/2026, 3:23:12 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        stk=[]
4        hashmap={')':'(',']':'[','}':'{'}
5        for i in s:
6            if i not in hashmap:
7                stk.append(i)
8            else:
9                if not stk:
10                    return False
11                else:
12                    popped=stk.pop()
13                    if popped!=hashmap[i]:
14                        return False
15        return not stk