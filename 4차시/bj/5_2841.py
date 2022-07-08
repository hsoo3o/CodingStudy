import sys
n,p = map(int,sys.stdin.readline().split())
cnt = 0
g = {i+1:[] for i in range(6)}

for _ in range(n):
    s,p = map(int,sys.stdin.readline().split())
    if len(g[s]) > 0:
        if g[s][-1] < p :
            cnt += 1
            g[s].append(p)
        else:
            while len(g[s]) > 0:
                if g[s][-1] <= p:
                    break
                g[s].pop()
                cnt += 1
            if len(g[s])==0:
                cnt += 1
                g[s].append(p)
            elif g[s][-1] < p:
                cnt += 1
                g[s].append(p)
    else:
        g[s].append(p)
        cnt += 1

print(cnt)


