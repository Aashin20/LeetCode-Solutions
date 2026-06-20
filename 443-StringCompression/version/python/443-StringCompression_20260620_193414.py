# Last updated: 6/20/2026, 7:34:14 PM
1class Solution:
2    def compress(self, chars: List[str]) -> int:
3        i=0
4        ins=0
5        while i<len(chars):
6            count=1
7            while (i+count)<len(chars) and chars[i+count]==chars[i]:
8                count+=1
9            chars[ins]=chars[i]
10            ins+=1
11            if count>1:
12                string=str(count)
13                chars[ins:ins+len(string)]=list(string)
14                ins+=len(string)
15            i+=count
16        return ins
17
18