# Last updated: 7/26/2025, 11:11:02 PM
from typing import List

class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        
     
        right = [[] for _ in range(n + 1)]
        for a, b in conflictingPairs:
            right[max(a, b)].append(min(a, b))
        
 
        ans = 0 
       
        left = [0, 0] 
    
        bonus = [0] * (n + 1)
        
      
        for r in range(1, n + 1):
            
            for l in right[r]:
              
                if l > left[0]:
                    left = [l, left[0]]
                elif l > left[1]:
                    left = [left[0], l]
            
          
            ans += r - left[0]

            if left[0] > 0:
                bonus[left[0]] += left[0] - left[1]
        
        return ans + max(bonus)