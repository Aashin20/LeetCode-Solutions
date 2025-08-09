# Last updated: 8/9/2025, 11:56:13 PM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & (n - 1))