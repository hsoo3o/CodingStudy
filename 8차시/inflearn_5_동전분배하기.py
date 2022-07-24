N = int(input())
money = []
for i in range(N):
    money.append(int(input()))
    
ans = 999999999
def dfs(L,p1,p2,p3):
    global ans
    if L == N:
        if p1 == p2 or p2 == p3 or p1 == p3:
            return
        elif p1 == 0 or p2 == 0 or p3 == 0:
            return
        else:
            p = [p1,p2,p3]
            max_p = max(p)
            min_p = min(p)
            pp = max_p - min_p
            if pp < ans:
                ans = pp
            return
    else:
        dfs(L+1, p1+ money[L],p2,p3)
        dfs(L+1, p1,p2+ money[L],p3)
        dfs(L+1,p1,p2,p3+ money[L])
    return



dfs(0,0,0,0)

print(ans)