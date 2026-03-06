# Last updated: 3/6/2026, 9:35:44 PM
1class Solution:
2    def validPalindrome(self, s: str) -> bool:
3        L = 0
4        R = len(s)-1
5        while L<R:
6            if s[L]!=s[R]:
7                skipL,skipR = s[L+1:R+1],s[L:R]
8                return (skipL==skipL[::-1] or skipR==skipR[::-1])
9            L+=1
10            R-=1
11        return True