# Last updated: 6/14/2025, 10:33:17 PM
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        L=1
        R=num
        while L<=R:
            M=(L+R)//2
            if M**2==num:
                return True
            elif M**2>num:
                R=M-1
            else:
                L=M+1
        return False