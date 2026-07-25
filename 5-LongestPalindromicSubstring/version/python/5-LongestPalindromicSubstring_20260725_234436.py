# Last updated: 7/25/2026, 11:44:36 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        odd=even=a=b=""
4        for i in range(len(s)):
5            a=self.count_palindrome(s,i,i)
6            b=self.count_palindrome(s,i,i+1)
7            if len(a)>len(odd):
8                odd=a
9            if len(b)>len(even):
10                even=b
11        if len(odd)>len(even): return odd
12        else: return even
13    def count_palindrome(self,s,L,R):
14        longest=0
15        while L>=0 and R<len(s) and s[L]==s[R]:
16            L-=1
17            R+=1
18        longest=s[L+1:R]
19        return longest
20    