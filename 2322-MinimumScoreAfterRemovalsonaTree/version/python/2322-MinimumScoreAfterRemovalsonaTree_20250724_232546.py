# Last updated: 7/24/2025, 11:25:46 PM
class Solution:
    def minimumScore(_,N,E):
     n=len(N);g=[[]for _ in N]
     for u,v in E:g[u]+=[v];g[v]+=[u]
     s=[0]*n;d=[0]*n
     def D(u,p):
      s[u],d[u]=N[u],1<<u
      for v in g[u]:
       if v-p:D(v,u);s[u]^=s[v];d[u]|=d[v]
     D(0,-1)
     r,t=9e9,s[0]
     for i in range(1,n):
      for j in range(i+1,n):
       x,y=s[i],s[j]
       k=(y,x^y,t^x)if d[i]>>j&1 else(x,y^x,t^y)if d[j]>>i&1 else(x,y,t^x^y)
       r=min(r,max(k)-min(k))
     return r