
import sys


def BFS(v):
    if v == m:
        for i in range(m):
            print(res[i],end=' ')
        print()
    else:
        for i in range(1,n+1):
            res[v] = i
            BFS(v+1)


n,m = map(int,sys.stdin.readline().split())
res = [0]*n
BFS(0)