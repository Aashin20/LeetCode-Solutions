# Last updated: 6/5/2026, 10:37:12 PM
1class Solution:
2    def evalRPN(self, tokens: List[str]) -> int:
3        stk=[]
4        for i in tokens:
5            if i in ['+','-','*','/']:
6                b=stk.pop()
7                a=stk.pop()
8                if i=='+':
9                    stk.append(a+b)
10                elif i=='-':
11                    stk.append(a-b)
12                elif i=='*':
13                    stk.append(a*b)
14                elif i=='/':
15                    stk.append(int(a/b))     
16            else:
17                stk.append(int(i))
18        return stk[0]        