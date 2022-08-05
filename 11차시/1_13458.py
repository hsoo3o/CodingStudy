n = int(input())
classroom = list(map(int, input().split()))
b,c = map(int, input().split())

ans = n
for i in range(n):
    boo = classroom[i]-b
    if boo > 0 :
        if boo %c != 0:
            ans += boo // c +1
        elif boo % c == 0:
            ans += boo // c 

print(ans)