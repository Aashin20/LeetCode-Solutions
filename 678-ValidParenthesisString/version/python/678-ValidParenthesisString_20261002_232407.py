# Last updated: 10/2/2026, 11:24:07 PM
1class Solution:
2    def checkValidString(self, s: str) -> bool:
3        leftMin=leftMax=0
4        for i in s:
5            if i=='(':
6                leftMax,leftMin=leftMax+1,leftMin+1
7            elif i==')':
8                leftMax,leftMin=leftMax-1,leftMin-1
9            else:
10                leftMax,leftMin=leftMax+1,leftMin-1
11            if leftMax<0:
12                return False
13            if leftMin<0: leftMin=0
14        return leftMin==0
15