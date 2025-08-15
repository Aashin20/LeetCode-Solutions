# Last updated: 8/16/2025, 1:10:50 AM
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return (n & (n - 1)) == 0 and n % 3 == 1