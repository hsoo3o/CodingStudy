
def dfs(l,sum_):
    global res
    if l == k:
        if 0< sum_ <= s:
            res.add(sum_)
        
    else:
        dfs(l+1,sum_+w[l])
        dfs(l+1,sum_ - w[l])
        dfs(l+1,sum_)



k = int(input())
w = list(map(int,input().split()))
s = sum(w)
res = set()
dfs(0,0)

print(s-len(res))