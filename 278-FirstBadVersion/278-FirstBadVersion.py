# Last updated: 6/14/2025, 10:33:25 PM
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
import array
class Solution:
    def firstBadVersion(self, n: int) -> int:
        L=1
        R=n
        while L<R:
            M=(L+R)//2
            if isBadVersion(M):
                R=M
            else:
                L=M+1
        
        return L
        