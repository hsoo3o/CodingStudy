import sys
t = int(sys.stdin.readline())
def check(num,n):
    for i in range(n):
        for j in range(i+1,n):
            if num[j][:len(num[i])] == num[i]:
                return False
    return True

for _ in range(t):
    n = int(sys.stdin.readline())
    num = []
    for _ in range(n):
        num.append(sys.stdin.readline().rstrip())
    num.sort(key=len)
    if check(num,n):
        print("YES")
    else:
        print("NO")