# Last updated: 6/14/2025, 10:32:13 PM
from collections import Counter
class Solution:
    def robotWithString(self, s: str) -> str:
        

        freq = Counter(s)
        st = []
        res = []
        
        def min_char(freq):
            for i in range(26):
                ch = chr(ord('a') + i)
                if freq[ch] > 0:
                    return ch
            return 'a'

        for ch in s:
            st.append(ch)
            freq[ch] -= 1
            while st and st[-1] <= min_char(freq):
                res.append(st.pop())

        while st:
            res.append(st.pop())

        return ''.join(res)
