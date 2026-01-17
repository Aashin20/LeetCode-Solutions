# Last updated: 1/17/2026, 8:28:55 PM
1class Solution:
2    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
3        quality = -1
4        best = [-1,-1]
5        for i in towers:
6            x,y,q=i
7            distance = abs(x-center[0])+abs(y-center[1])
8            if distance <= radius:
9                if quality<q:
10                    quality=q
11                    best = [x,y]
12                elif q==quality:
13                    if best==[-1,-1] or x<best[0] or (x==best[0] and y<best[1]):
14                        best = [x,y]
15        return best
16                
17                