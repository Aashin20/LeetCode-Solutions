# Last updated: 6/14/2025, 10:33:20 PM
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        l=0
        r=n-1
        while l<r:
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        