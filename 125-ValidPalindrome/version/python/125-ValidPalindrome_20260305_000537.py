# Last updated: 3/5/2026, 12:05:37 AM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        st = ''.join(s.split()).lower()
4        result = ''.join([char for char in st if char.isalnum()])
5        return result == result[::-1]