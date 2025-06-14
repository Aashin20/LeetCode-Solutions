# Last updated: 6/14/2025, 10:33:51 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = list(map(str.lower, filter(str.isalnum, s)))
        left=0
        right=len(l)-1
        while left<right:
            if l[left]!=l[right]:
                return False
                break
                
            else:
                left+=1
                right-=1
                continue
        return True
