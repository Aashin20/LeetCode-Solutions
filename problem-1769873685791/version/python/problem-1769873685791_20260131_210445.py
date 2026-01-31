# Last updated: 1/31/2026, 9:04:45 PM
1class Solution:
2    def reverseByType(self, s: str) -> str:
3        arr=list(s)
4        L,R=0,len(arr)-1
5        while L<R:
6            if not ('a' <= arr[L] <= 'z'):
7                L += 1
8            elif not ('a' <= arr[R] <= 'z'):
9                R -= 1
10            else:
11                arr[L], arr[R] = arr[R], arr[L]
12                L += 1
13                R -= 1
14        L,R=0,len(s)-1
15        while L<R:
16            if 'a' <= arr[L] <= 'z':
17                L += 1
18            elif 'a' <= arr[R] <= 'z':
19                R -= 1
20            else:
21                arr[L], arr[R] = arr[R], arr[L]
22                L += 1
23                R -= 1
24        return ''.join(arr)