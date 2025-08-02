# Last updated: 8/2/2025, 12:47:56 PM
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=1
        r=n
        while l<r:
            mid=(l+r)//2
            if isBadVersion(mid)==True:
                r=mid
            else:
                l=mid+1
        return l