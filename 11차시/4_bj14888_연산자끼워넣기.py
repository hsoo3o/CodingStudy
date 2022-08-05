import itertools

N = int(input())
A = list(map(int,input().split()))
l = list(map(int,input().split()))
ll = []

for idx,i in enumerate(l):
    if i != 0:
        if idx == 0:
            for j in range(i):
                ll.append("A")
        elif idx == 1:
            for j in range(i):
                ll.append("B")
        elif idx == 2:
            for j in range(i):
                ll.append("C")
        elif idx == 3:
            for j in range(i):
                ll.append("D")
ll = list(itertools.permutations(ll))
ans = []
for lll in ll:
    tmp = A[0]
    for i,llll in enumerate(lll):
        j = i+1
        if i == len(lll):
            break
        if llll == 'A':
            tmp += A[j]
        elif llll == 'B':
            tmp -= A[j]
        elif llll == 'C':
            tmp *= A[j]
        elif llll == 'D':
            if tmp < 0:
                tmp = -tmp
                tmp = tmp // A[j]
                tmp = -tmp
            else:
                tmp = tmp//A[j]
    ans.append(tmp)
print(max(ans))
print(min(ans))


# def dfs(L,which):
#     if L == N:
#         result.append()
#         return
#     else:
