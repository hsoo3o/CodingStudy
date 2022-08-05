import math
N = int(input())
A = list(map(int,input().split()))
B,C = map(int,input().split())
ans = 0
for n in A:
    n -= B
    if n <= 0:
        pass
    else:
        if n % C == 0:
            ans += n/C
        else:
            ans += n//C + 1
print(int(N + ans))