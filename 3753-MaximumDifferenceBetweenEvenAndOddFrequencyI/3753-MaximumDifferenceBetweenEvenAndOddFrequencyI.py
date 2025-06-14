# Last updated: 6/14/2025, 10:31:48 PM
class Solution:
    def maxDifference(self, s: str) -> int:
        record = Counter(s)

        max_odd = 0
        min_even = float('inf')
        for ch in record:
            if record[ch] % 2 != 0:
                max_odd = max(max_odd, record[ch])
            if record[ch] % 2 == 0:
                min_even = min(min_even, record[ch])
        return max_odd - min_even
        