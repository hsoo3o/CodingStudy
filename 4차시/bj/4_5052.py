import sys
t = int(sys.stdin.readline())
def check(num,n):
    for i in range(n-1):
        if num[i] == num[i+1][:len(num[i])]:
            return False
    return True

for _ in range(t):
    n = int(sys.stdin.readline())
    num = []
    for _ in range(n):
        num.append(sys.stdin.readline().rstrip())
    num.sort()
    if check(num,n):
        print("YES")
    else:
        print("NO")