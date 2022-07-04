n = int(input())
switch = list(map(int,input().split(' ')))

for _ in range(int(input())):
    a,b = map(int, input().split(' '))
    sumb = b
    if a == 1:
        while b <= n:
            if switch[b-1]:
                switch[b-1] = 0
            else:
                switch[b-1] = 1
            b += sumb
    else:
        i = 0
        while b+i <= n and b-i > 0:
            if switch[b-i-1] == 0 and switch[b+i-1] == 0:
                switch[b-i-1] = 1
                switch[b+i-1] = 1
            elif switch[b-i-1] == 1 and switch[b+i-1] == 1:
                switch[b-i-1] = 0
                switch[b+i-1] = 0
            else: 
                break
            i += 1
ans = str(switch[0])
for s in range(0,n,20):
    print(' '.join(map(str,switch[s:s+20])))
