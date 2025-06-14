# Last updated: 6/14/2025, 10:32:07 PM
class Solution:
    def minMaxDifference(self, num: int) -> int:
        replace_for_max = ''
        s=str(num)
        for c in s:
            if c != '9':
                replace_for_max = c
                break
        max_str = ''.join(['9' if c == replace_for_max else c for c in s])
        replace_for_min = s[0]
        min_str = ''.join(['0' if c == replace_for_min else c for c in s])

        return int(max_str) - int(min_str)