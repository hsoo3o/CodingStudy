import itertools as it
def dfs(l,s,sum_):
    global cnt
    if l == k:
        if sum_ % m == 0:

            cnt += 1
    else:
        for i in range(s,n):
            # res[l] = numlist[i]
            dfs(l+1,i+1, sum_ + numlist[i])


n,k = map(int,input().split())
cnt = 0
numlist = list(map(int,input().split()))
m = int(input())
# res = [0]*(k)
dfs(0,0,0)
print(cnt)

for x in it.combinations(numlist,k):
    if sum(x) % m == 0:
        cnt += 1
print(cnt)