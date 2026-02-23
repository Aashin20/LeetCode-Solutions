# Last updated: 2/23/2026, 10:18:10 PM
1class Solution:
2    def maximumXor(self, s: str, t: str) -> str:
3        n = len(s)
4        ones = t.count('1')
5        zeros = n - ones
6        
7        result = []
8        
9        for ch in s:
10            if ch == '0':
11                if ones > 0:
12                    result.append('1')
13                    ones -= 1
14                else:
15                    result.append('0')
16                    zeros -= 1
17            else:  
18                if zeros > 0:
19                    result.append('1')
20                    zeros -= 1
21                else:
22                    result.append('0')
23                    ones -= 1
24        
25        return ''.join(result)
26        
27        