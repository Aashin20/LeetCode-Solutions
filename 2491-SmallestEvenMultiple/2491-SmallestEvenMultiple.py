# Last updated: 6/14/2025, 10:32:20 PM
class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        i=1
        while(True):
            if(i%2==0 and i%n==0):
                return i
                break
            else:
                i+=1