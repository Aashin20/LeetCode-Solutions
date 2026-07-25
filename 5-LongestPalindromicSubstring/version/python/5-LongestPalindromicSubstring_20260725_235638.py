# Last updated: 7/25/2026, 11:56:38 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        longest = ""
4        for i in range(len(s)):
5            odd = self.expand(s, i, i)
6            even = self.expand(s, i, i + 1)
7
8            if len(odd) > len(longest):
9                longest = odd
10
11            if len(even) > len(longest):
12                longest = even
13
14        return longest
15
16    def expand(self, s, left, right):
17        while left >= 0 and right < len(s) and s[left] == s[right]:
18            left -= 1
19            right += 1
20
21        return s[left + 1:right]