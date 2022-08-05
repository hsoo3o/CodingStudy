import sys
def dfs(l,person,team):
    global case, ans, sum_, else_,ch
    case -= 1  
    if case == 0:
        return
    if l == n//2 -1:
        for t in team:
            ch.remove(t)
            for j in team:
                if t != j:
                    sum_ += s[t][j]
        for i in ch:
            for j in ch:
                if i != j :
                    else_ += s[i][j]
        if abs(sum_-else_) < ans:
            ans =  abs(sum_-else_)
        sum_ = 0
        else_ = 0
        ch = [i for i in range(n)]
    else:
        for i in range(person+1,n):
            dfs(l+1,i,team+[i])

n = int(input())
ch = [i for i in range(n)]
case = 1
for i in range(n//2):
    case = case * (n- i)
    case = case / (i+1)
case += 1
sum_ = 0
else_ = 0
ans = 214700000
s = []
for i in range(n):
    s.append(list(map(int,sys.stdin.readline().split())))

dfs(0,0,[0])
print(ans)