# Last updated: 6/13/2026, 12:36:49 PM
1class Solution:
2    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
3        ans = ''
4        
5        for word in words:
6            total = 0
7            for char in word:
8                total += weights[ord(char) - ord('a')]
9            
10            remainder = total % 26
11            ans += chr(ord('z') - remainder)
12        
13        return ans
14