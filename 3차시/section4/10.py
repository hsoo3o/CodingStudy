n = int(input())
num = list(map(int,input().split(' ')))
seq = [0]*n
for i in range(n):
    for j in range(n):
        if num[i] == 0 and seq[j] == 0:
            seq[j] = i+1
            break
        elif seq[j] == 0:
            num[i] -= 1
        

for x in seq:
    print(x, end=' ')