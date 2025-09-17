# Last updated: 9/17/2025, 10:25:31 PM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        count=[0]*26
        for r in range(len(s)):
            count[ord(s[r])-65]+=1
            while (r-l)+1 - max(count)>k:
                count[ord(s[l])-65]-=1
                l+=1
            longest = max(longest,r-l+1)
        return longest