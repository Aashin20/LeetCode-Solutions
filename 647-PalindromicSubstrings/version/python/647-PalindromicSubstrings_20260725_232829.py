# Last updated: 7/25/2026, 11:28:29 PM
1class Solution:
2    def countSubstrings(self, s: str) -> int:
3        res=0
4        for i in range(len(s)):
5            res+=self.count_palindrome(s,i,i)
6            res+=self.count_palindrome(s,i,i+1)
7        return res
8    def count_palindrome(self,s,L,R):
9            res=0
10            while L >= 0 and R < len(s) and s[L] == s[R]:
11                L-=1
12                R+=1
13                res+=1
14            return res
15        