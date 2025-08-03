# Last updated: 8/3/2025, 9:41:11 PM
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        time=0
        for i in range(len(points)-1):
            x1,y1=points[i]
            x2,y2=points[i+1]
            t=max(abs(x2-x1),abs(y2-y1))
            time+=t
        return time