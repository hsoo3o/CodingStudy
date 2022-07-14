import sys


def DFS(v):
    sum1,sum2 = 0,0
    if v == n+1:
        for i in range(1,n+1):
            if ch[i] == 1:
                sum1 += num[i-1]
            else:
                sum2 += num[i-1]
        if sum1 == sum2:
            print("YES")
            sys.exit(0)
    else:
        ch[v] = 1
        a = DFS(v+1)
        ch[v] = 0
        a = DFS(v+1)




n = int(input())
num = list(map(int,input().split()))
ch = [0]*(n+1)
DFS(1)

print("NO")