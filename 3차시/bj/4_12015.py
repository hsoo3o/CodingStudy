import sys
n = int(input())

anum = list(map(int, sys.stdin.readline().split(' ')))
all_ans = []
ans = 0
res = [0]
for j in range(n-1):
    num = anum[j:]
    ans = 0
    res = [0]
    for i in range(len(num)-1):
        if num[i] <= num[i+1] and num[i] >= res[-1]:
            ans += 1
            res.append(num[i])

    if num[-1] >= res[-1]:
        ans += 1
    all_ans.append(ans)
print(max(all_ans))

4,7,10