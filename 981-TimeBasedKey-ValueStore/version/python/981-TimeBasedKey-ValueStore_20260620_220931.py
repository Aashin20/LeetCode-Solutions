# Last updated: 6/20/2026, 10:09:31 PM
1class TimeMap:
2
3    def __init__(self):
4        self.store={}
5
6    def set(self, key: str, value: str, timestamp: int) -> None:
7        if key not in self.store:
8            self.store[key]=[]
9        self.store[key].append([value,timestamp])
10
11    def get(self, key: str, timestamp: int) -> str:
12        res=""
13        values=self.store.get(key,[])
14        L=0
15        R=len(values)-1
16        while L<=R:
17            mid=(L+R)//2
18            if values[mid][1]<=timestamp:
19                res=values[mid][0]
20                L=mid+1
21            else:
22                R=mid-1
23        return res
24# Your TimeMap object will be instantiated and called as such:
25# obj = TimeMap()
26# obj.set(key,value,timestamp)
27# param_2 = obj.get(key,timestamp)