
import itertools as it
import sys


def DFS(v,sum_):
    if v == n and sum_ == f:
        for i in res:
            print(i,end=' ')
        sys.exit(0)
    else:
        for i in range(1,n+1):
            if ch[i] != 1:
                ch[i] = 1
                res[v] = i
                DFS(v+1 ,sum_+i*b[v])
                ch[i] = 0
    
n,f = map(int,input().split())


b = [1]*n
ch = [0]*(n+1)
res = [0]*(n)

for i in range(1,n):
    b[i] = b[i-1]*(n-i) // i

DFS(0,0)


a = list(range(1,n+1))
for tmp in it.permutations(a):
    sum_ = 0
    for l,x in enumerate(tmp):
        sum_ += (x*b[l])
    if sum_ == f:
        for x in tmp:
            print(x,end=' ')
        break